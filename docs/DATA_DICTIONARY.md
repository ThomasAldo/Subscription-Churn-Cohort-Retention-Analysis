# 📊 Data Dictionary

Comprehensive field-level documentation for all datasets in the Subscription Churn & Retention Dashboard project.

---

## 📥 Master Dataset: portfolio_subscription_master.csv

**Purpose:** Raw transaction-level subscription data used for RFM calculation and churn model training.

**Volume:** 1,003,025 rows | **Period:** January 2015 – March 2017 | **Granularity:** One row per transaction

| Column | Data Type | Range/Values | Description | Business Context |
|--------|-----------|--------------|-------------|------------------|
| **customer_id** | String (hashed) | 60,000 unique values | Unique customer identifier (hashed for privacy) | Links all transactions to a single customer; enables customer-level aggregation |
| **churn_status** | Integer (0/1) | 0 or 1 | 0 = active/retained, 1 = churned | Target variable for model training; defines churn outcome |
| **payment_date** | Date (DD-MM-YYYY) | 01-01-2015 to 31-03-2017 | Date of subscription payment/renewal | Used to calculate Recency; establishes transaction timeline |
| **expire_date** | Date (DD-MM-YYYY) | 01-01-2015 to 31-05-2017 | Subscription expiration/renewal date | Identifies when renewal was due; flags customers approaching expiration |
| **amount** | Float (USD) | $0–$10,000+ | Transaction amount in dollars | Used to calculate Monetary; indicates customer value per transaction |
| **is_auto_renew** | Integer (0/1) | 0 or 1 | 1 = auto-renewal enabled, 0 = manual renewal | Behavioral flag; indicates subscription renewal automation preference |
| **is_cancel** | Integer (0/1) | 0 or 1 | 1 = cancellation detected, 0 = normal transaction | Behavioral flag; signals cancellation intent or churn risk |

**Key Notes:**
- Multiple rows per customer (transaction level); aggregated to customer-level for RFM
- **Recency:** Calculated as days from MAX(payment_date) in dataset (31-Mar-2017) to each customer's last payment_date
- **Monetary:** SUM(amount) per customer across entire dataset window (Jan 2015–Mar 2017)

---

## 📊 RFM Segmentation Output: rfm_segmentation_output.csv

**Purpose:** Customer-level aggregated RFM metrics with churn probability predictions and risk classification.

**Volume:** 60,000 rows (one per unique customer) | **Derived from:** portfolio_subscription_master.csv

| Column | Data Type | Range | Description | Calculation |
|--------|-----------|-------|-------------|-------------|
| **customer_id** | String (hashed) | 60,000 unique | Links to master dataset | Primary key; join field to master data |
| **Recency** | Integer | 0–500+ days | Days since last transaction | `MAX(analysis_date) - MAX(customer's payment_date)` |
| **Frequency** | Integer | 1–500+ transactions | Number of transactions in window | `COUNT(payment_date)` per customer |
| **Monetary** | Float (USD) | $0–$10,000+ | Total customer spend (Jan 2015–Mar 2017) | `SUM(amount)` per customer |
| **RFM_Segment** | String | 3-digit code (e.g., "114", "314") | Behavioral segment code | Each digit represents Recency, Frequency, Monetary tier (1–9) |
| **Churn_Probability** | Float | 0.0–1.0 | ML model prediction of churn likelihood | Output from churn probability model |
| **Risk_Level** | String | "High Risk (>40%)" or "Low/Medium Risk" | Risk classification | "High Risk" if Churn_Probability > 0.40 |

---

## 📈 Cohort Retention Output: sql_cohort_retention_output.csv

**Purpose:** Historical cohort-based retention tracking; validates churn model accuracy.

**Volume:** 28 rows (cohorts) × 20 columns (months 0–19) | **Period:** Jan 2015–Mar 2017 cohorts

| Column | Data Type | Range | Description |
|--------|-----------|-------|-------------|
| **Cohort_Month** | String (Month, Year) | Jan 2015–Mar 2017 | Cohort assignment month (first transaction) |
| **Month_0 through Month_19** | Float (%) | 50–100% | Retention % at each month offset |

**Key Metrics:**
- **Avg Retention Rate:** 87.16%
- **Highest retention:** ~96% (renewal windows)
- **Cyclical Pattern:** Spikes at months 3, 6, 12

---

## 🎯 Dashboard Metrics & Calculations

### High-Risk Customers
```
COUNTIF(rfm_segmentation_output.Churn_Probability > 0.40) = 1,436
```

### At-Risk Revenue
```
SUM(Monetary) WHERE Churn_Probability > 0.40 = $3.56M
```

### Projected Revenue Saved
```
At-Risk Revenue × Retention Success Rate = Projected Savings
Example: $3.56M × 15% = $534K
```

---

## 🔐 Data Quality & Privacy

- **Missing Values:** Handled; nulls treated as 0 or default
- **Outliers:** Extreme values (>$10K) kept as valid (premium customers)
- **Privacy:** customer_id hashed; no real names or emails exposed
- **Assumptions:** Analysis date fixed at 31-Mar-2017; Monetary window = full dataset
