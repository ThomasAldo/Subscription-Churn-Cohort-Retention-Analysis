import pandas as pd
import numpy as np

print("1. Loading Master Dataset...")
df = pd.read_csv('portfolio_subscription_master.csv')
df['payment_date'] = pd.to_datetime(df['payment_date'])

# Set the "current date" to the max date in the dataset (approx March 31, 2017)
snapshot_date = df['payment_date'].max() + pd.Timedelta(days=1)

print("2. Calculating R, F, M metrics per customer...")
rfm = df.groupby('customer_id').agg({
    'payment_date': lambda x: (snapshot_date - x.max()).days,  # Recency (Days since last payment)
    'customer_id': 'count',                                    # Frequency (Total transactions)
    'amount': 'sum',                                           # Monetary (Total spend)
    'churn_status': 'max'                                      # Carry over the churn flag (1=churn, 0=renewed)
}).rename(columns={
    'payment_date': 'Recency',
    'customer_id': 'Frequency',
    'amount': 'Monetary'
}).reset_index()

print("3. Scoring RFM out of 4 (Quartiles)...")
# For Recency: Lower days is BETTER (Score 4 is best, 1 is worst)
rfm['R_Score'] = pd.qcut(rfm['Recency'], q=4, labels=[4, 3, 2, 1], duplicates='drop')

# For Frequency & Monetary: Higher is BETTER (Score 4 is best, 1 is worst)
# Note: Using rank to handle duplicate frequency counts smoothly
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=4, labels=[1, 2, 3, 4])
rfm['M_Score'] = pd.qcut(rfm['Monetary'].rank(method='first'), q=4, labels=[1, 2, 3, 4])

# Combine into a single string segment (e.g., '111', '444')
rfm['RFM_Segment'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

print("4. Identifying High-Risk Cohorts...")
# Calculate the churn rate for every segment
segment_churn = rfm.groupby('RFM_Segment')['churn_status'].mean().reset_index()
segment_churn.rename(columns={'churn_status': 'Churn_Probability'}, inplace=True)

# Merge probabilities back into the main dataset
rfm = pd.merge(rfm, segment_churn, on='RFM_Segment', how='left')

# Flag the specific cohorts that exhibit > 40% churn probability
rfm['Risk_Level'] = np.where(rfm['Churn_Probability'] >= 0.40, 'High Risk (>40% Churn)', 'Low/Medium Risk')

print("5. Exporting for Power BI...")
rfm.to_csv('rfm_segmentation_output.csv', index=False)

# Quick summary for your sanity check
high_risk_count = rfm[rfm['Risk_Level'] == 'High Risk (>40% Churn)']['RFM_Segment'].nunique()
print(f"\nSuccess! Found {high_risk_count} segments with >40% churn risk.")
print("\nPreview of RFM output:")
print(rfm[['customer_id', 'RFM_Segment', 'Churn_Probability', 'Risk_Level']].head(10))