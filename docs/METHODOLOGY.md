# 📊 Methodology: RFM Segmentation & Churn Prediction Model

Complete technical documentation of the RFM framework, churn probability model, and validation approach used in this project.

---

## 1️⃣ RFM Framework Overview

### What is RFM?

**RFM** is a customer segmentation methodology that classifies customers into behavioral groups based on three key metrics:

- **Recency (R):** How recently a customer engaged/made a purchase
- **Frequency (F):** How often a customer engaged/made purchases
- **Monetary (M):** How much money a customer spent

### Why RFM?

✔ **Simple & Interpretable** — Easy to understand and explain to non-technical stakeholders

✔ **Actionable** — Each segment suggests targeted retention tactics (win-back, upsell, etc.)

✔ **Predictive of Churn** — Recent, frequent, high-value customers are less likely to churn

✔ **Lightweight** — No complex feature engineering required; works with transaction data alone

---

## 2️⃣ RFM Calculation Details

### Data Source
- **Input:** `portfolio_subscription_master.csv` (1,003,025 transaction rows)
- **Period:** January 2015 – March 2017 (27 months)
- **Analysis Date:** March 31, 2017 (max date in dataset)

### Recency (R) Calculation

```
R_days = Analysis_Date - MAX(customer's payment_date)
```

**Example:**
- Analysis Date: 2017-03-31
- Customer's Last Payment: 2017-01-15
- Recency: 31 - 15 = 75 days since last purchase

**Interpretation:**
- **Low R (0–30 days):** Recently active → High engagement
- **High R (100+ days):** Inactive/lapsed → Churn risk

**Scoring:** 1–9 scale (inverted)
- Recency 0–30 days → Score 9 (excellent)
- Recency 30–60 days → Score 7
- Recency 100+ days → Score 1 (poor)

### Frequency (F) Calculation

```
F_count = COUNT(distinct payment_date) per customer in dataset window
```

**Example:**
- Customer paid on: 2015-02-01, 2015-05-15, 2016-01-10, 2017-02-20
- Frequency: 4 transactions

**Interpretation:**
- **Low F (1–2 transactions):** Light user, rare engagement → Risk if also low recency
- **High F (10+ transactions):** Loyal, recurring customer → Lower churn likelihood

**Scoring:** 1–9 scale (direct)
- Frequency 1–2 → Score 1 (poor)
- Frequency 3–5 → Score 5 (medium)
- Frequency 10+ → Score 9 (excellent)

### Monetary (M) Calculation

```
M_sum = SUM(amount) per customer across full dataset window (Jan 2015–Mar 2017)
```

**Example:**
- Customer transactions: $149 (Feb 2015), $149 (May 2015), $149 (Jan 2016), $149 (Mar 2017)
- Monetary: $596 total spend

**Interpretation:**
- **Low M ($0–$500):** Cheap/budget customer → May have low tolerance for price increases
- **High M ($5,000+):** Premium customer → High priority to retain (large revenue impact)

**Scoring:** 1–9 scale (direct)
- Monetary $0–$500 → Score 1
- Monetary $1,000–$3,000 → Score 5
- Monetary $5,000+ → Score 9

### RFM Segment Code

Each customer assigned a **3-digit code** combining R, F, M scores:

```
RFM_Segment = [R_score][F_score][M_score]

Example: Customer with R=3, F=1, M=4 → Segment "314"
```

**Segment Interpretation Grid:**

| Segment | Recency | Frequency | Monetary | Profile | Retention Strategy |
|---------|---------|-----------|----------|---------|-------------------|
| **111** | High (poor) | Low | Low | Lost/Dormant | Win-back campaign (low ROI) |
| **114** | High | Low | Medium | Cheap & lapsed | Light win-back (modest value) |
| **314** | Medium | Low | High | **High-value lapsed** | **Urgent relationship recovery** |
| **414** | Low | Low | High | **Recent high-value** | Upsell/cross-sell opportunity |
| **777** | Low | High | High | **VIP** | **Premium support, prevent churn** |
| **911** | Very recent | Low | Low | New customer | Onboarding/engagement |
| **999** | Very recent | Very high | Very high | **Top champion** | **Loyalty program, advocate** |

---

## 3️⃣ Churn Probability Model

### Model Architecture

**Type:** Supervised Classification (Binary: Churn Yes/No)

**Input Features:**
1. RFM Metrics (3 features):
   - Recency (days)
   - Frequency (count)
   - Monetary (dollars)

2. Behavioral Flags (2 features):
   - is_auto_renew (0/1) — Whether auto-renewal enabled
   - is_cancel (0/1) — Whether cancellation detected

3. Subscription Status (1 feature):
   - Days to expiration — Time until next renewal

**Total Features:** 6

**Target Variable:** churn_status (0 = active, 1 = churned)

### Model Training Process

```python
# Pseudocode
from sklearn.ensemble import RandomForestClassifier

# 1. Prepare features & target
X = [Recency, Frequency, Monetary, is_auto_renew, is_cancel, days_to_expiry]
y = churn_status

# 2. Train-test split (optional, for validation)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Generate predictions
churn_probability = model.predict_proba(X)[:, 1]  # Probability of churn (class 1)

# 5. Classification with threshold
risk_level = "High Risk" if churn_probability > 0.40 else "Low/Medium Risk"
```

### Output: Churn Probability

**Range:** 0.0 to 1.0

- **0.0–0.2:** Very low churn risk (unlikely to churn)
- **0.2–0.4:** Low/medium churn risk (stable customer)
- **0.4–0.7:** High churn risk (intervention recommended)
- **0.7–1.0:** Very high churn risk (urgent intervention)

**Decision Threshold:** 0.40
- Customers with Churn_Probability > 0.40 classified as **"High Risk"**
- Customers with Churn_Probability ≤ 0.40 classified as **"Low/Medium Risk"**

---

## 4️⃣ Model Validation

### Validation Approach

Since this project uses historical data, model performance is validated through **cohort analysis** and **distribution inspection**.

### 1. Churn Probability Distribution Validation

**Dashboard Visual:** Histogram on Page 2

**What We Observe:**
- **Bimodal distribution** with peaks at low probability (0.0–0.1) and high probability (0.7–1.0)
- **Clear separation at 0.40 threshold** — few customers in 0.4–0.6 range
- **Interpretation:** Model produces confident predictions; threshold is appropriate

**Expected Pattern:**
- Low-risk cohort (0.0–0.2): ~58,564 customers (97.61%)
- High-risk cohort (0.7–1.0): ~1,436 customers (2.39%)

### 2. Cohort Retention Matrix Validation

**Dashboard Visual:** Cohort matrix on Page 1

**Validation Logic:**
- **Model Output:** Churn probability estimates propensity to churn
- **Observed Behavior:** Cohort retention matrix shows actual churn over time
- **Alignment:** If model is accurate, high-risk customers should show lower retention in cohorts

**Key Findings:**
- **Avg Retention Rate:** 87.16% across all cohorts
- **Cyclical Pattern:** Spikes at months 3, 6, 12 (quarterly/annual renewal windows)
- **Implication:** Model captures renewal-driven churn; not random attrition

**Cohort Interpretation:**
- January 2015 cohort, Month 0: 100.00% (baseline)
- January 2015 cohort, Month 1: 96.90% → 3.1% attrition at 1-month mark
- January 2015 cohort, Month 12: 78.15% → 21.85% cumulative attrition at 1-year mark

### 3. Feature Importance

**Expected Feature Impact on Churn:**

| Feature | Impact | Direction |
|---------|--------|-----------|
| **Recency** | High | ↑ (high recency = high churn probability) |
| **Frequency** | High | ↓ (high frequency = low churn probability) |
| **Monetary** | Medium | ↓ (high monetary = lower churn risk) |
| **is_auto_renew** | Medium | ↓ (auto-renew enabled = lower churn) |
| **is_cancel** | High | ↑ (cancellation flag = high churn) |
| **days_to_expiry** | Medium | ↑ (near expiration = higher risk) |

---

## 5️⃣ Risk Threshold Selection (0.40)

### Why 0.40?

**Analysis:**
1. **Business Context:** High-Risk segment should be manageable size (~2–5% of customer base)
   - 1,436 customers / 60,000 total = 2.39% ✓ (reasonable intervention scale)

2. **Distribution Inspection:** Natural gap in probability distribution around 0.40
   - Few customers in 0.35–0.50 range (clear separation)
   - Majority below 0.35 or above 0.65

3. **ROI Trade-off:**
   - **Too low threshold (0.25):** Overclassify as high-risk, waste resources on low-probability churn
   - **Too high threshold (0.60):** Underclassify risk, miss at-risk customers
   - **0.40 threshold:** Balanced false positive/false negative trade-off

### Sensitivity Analysis

**If threshold = 0.30:**
- High-Risk count: ~3,000 customers
- At-Risk Revenue: ~$5M
- Issue: Too many false positives (resource intensive)

**If threshold = 0.50:**
- High-Risk count: ~800 customers
- At-Risk Revenue: ~$2M
- Issue: May miss true at-risk customers (false negatives)

**Current (0.40):**
- High-Risk count: ~1,436 customers
- At-Risk Revenue: $3.56M
- Balanced approach ✓

---

## 6️⃣ Scenario Planning: ROI Modeling

### Formula

```
Projected Revenue Saved = At-Risk Revenue × Retention Success Rate
```

**Components:**
- **At-Risk Revenue:** $3.56M (sum of Monetary for all High-Risk customers)
- **Retention Success Rate:** % of at-risk customers successfully retained (slider: 0–100%)
- **Projected Savings:** Direct revenue impact of intervention

### Examples

| Retention Success % | Projected Savings | Business Interpretation |
|-------------------|-------------------|------------------------|
| 5% | $178K | Minimal intervention (break-even with low effort) |
| 15% | $534K | Conservative (realistic with email + phone outreach) |
| 25% | $890K | Good (requires relationship manager involvement) |
| 50% | $1.78M | Optimistic (requires high-touch, personalized approach) |
| 100% | $3.56M | Unrealistic (retain all at-risk customers) |

### Use Case: Budget Justification

**Executive Question:** "How much should we spend on retention campaigns?"

**Data-Driven Answer:**
- "We can identify $3.56M at-risk revenue from 1,436 customers."
- "If we retain just 15% (215 customers), we save $534K."
- "To justify $50K campaign spend, we need to retain only 15% of at-risk customers (ROI = 10.7x)."

---

## 7️⃣ Behavioral Targeting Recommendations

### RFM-Based Tactics

Using RFM segment codes, tailor retention strategy:

#### **Segment 314: Lapsed High-Value** (Low R, Low F, High M)
- **Churn Risk:** EXTREME (largest revenue impact if lost)
- **Tactic:** Urgent relationship recovery
- **Action:** Executive-level outreach, custom retention offer, root cause analysis
- **Timing:** Immediate (before further lapse)

#### **Segment 114: Lapsed Low-Value** (High R, Low F, Low M)
- **Churn Risk:** Low (but unhealthy trend)
- **Tactic:** Win-back campaign (low budget)
- **Action:** Email nurture sequence, re-engagement incentive
- **Timing:** Quarterly (cost-effective batch)

#### **Segment 414: Recent High-Value** (Low R, Low F, High M)
- **Churn Risk:** Medium (newly acquired, may still explore)
- **Tactic:** Onboarding + upsell
- **Action:** Educational content, premium feature trial, success manager assignment
- **Timing:** First 30 days (critical onboarding window)

#### **Segment 777: VIP** (Low R, High F, High M)
- **Churn Risk:** Low (but disproportionate impact if lost)
- **Tactic:** Loyalty & advocacy
- **Action:** VIP program, priority support, exclusive features
- **Timing:** Ongoing (preventive)

---

## 8️⃣ Known Limitations & Future Work

### Current Limitations

1. **Static Model:** Trained on historical data; does not auto-update
   - **Fix:** Implement monthly retraining pipeline

2. **No Feature Interaction:** Model treats features independently
   - **Fix:** Add polynomial features, interaction terms (e.g., Recency × is_cancel)

3. **No Temporal Dynamics:** Does not account for trends (e.g., is churn accelerating?)
   - **Fix:** Add time-series features, trend indicators

4. **Imbalanced Classes:** Churn (1) is rare (~25% in dataset)
   - **Fix:** Apply SMOTE, class weights, or threshold optimization

5. **Limited Feature Set:** Only uses transactional RFM + 3 behavioral flags
   - **Fix:** Add customer support interactions, product usage, NPS

### Future Enhancements

🔮 **Real-Time Churn Alerts:** Trigger when customer crosses 0.40 threshold

🔮 **Propensity-to-Buy Model:** Complement churn with upsell opportunities

🔮 **Cohort-Specific Models:** Different models for customer segments (B2B vs B2C, etc.)

🔮 **Causal Analysis:** Identify what *causes* churn, not just correlation

🔮 **Survival Analysis:** Model time-to-churn, not just binary outcome

---

## 📋 References

**RFM Framework:**
- Pareto, V. (1906). "Manual of Political Economy"
- Pfeifer, P. E., & Carraway, R. L. (2000). "Modeling customer relationships as Markov chains"

**Churn Prediction:**
- Larivière, B., & Van den Poel, D. (2005). "Predicting customer retention and profitability"
- Verbeke, W., et al. (2012). "New insights into churn prediction in the telecommunication sector"

**Model Validation:**
- Fawcett, T. (2006). "An introduction to ROC analysis"

---

## 🔗 Related Documentation

- [README.md](../README.md) — Project overview
- [DATA_DICTIONARY.md](DATA_DICTIONARY.md) — Field definitions
- [insights_recommendations.md](insights_recommendations.md) — Executive summary
