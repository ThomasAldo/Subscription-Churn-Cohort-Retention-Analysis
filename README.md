<p align="center"> 
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FF6B6B,50:EE5A6F,100:C92A2A&height=200&section=header&text=Subscription%20Churn%20%26%20Retention%20Dashboard&fontSize=38&fontColor=ffffff&fontAlignY=55"/> 
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37726?style=for-the-badge&logo=jupyter&logoColor=white"/>
</p>

---

# 📊 Project Overview

The **Subscription Churn & Retention Dashboard** is an end-to-end predictive analytics solution that transforms subscription transaction data into actionable retention strategy. Using RFM segmentation and machine learning-based churn probability modeling, this project enables data-driven customer retention planning.

**Real Business Impact:** Identify **1,436 high-risk customers** worth **$3.56M** in potential revenue loss and execute targeted retention campaigns with **ROI quantification**.

---

# 💼 Business Problem

Modern subscription businesses face critical challenges:

❌ **Hidden Churn Risk** — Inability to identify which customers are likely to churn before it happens

❌ **Revenue Exposure Blind Spot** — Unclear which customer segments represent the biggest financial loss

❌ **Inefficient Retention** — Applying uniform retention tactics instead of targeted, data-driven strategies

❌ **No ROI Clarity** — Retention teams can't quantify expected savings or justify intervention budgets

❌ **Reactive, Not Proactive** — Churn discovered after it happens, not predicted in advance

Without predictive analytics, retention teams work blind—wasting budget on low-risk customers while missing high-value at-risk cohorts.

---

# ✅ Business Solution

## This Dashboard Delivers:

✔ **Churn Probability Model** — ML-based prediction of customer churn risk (0–1 scale)

✔ **RFM Segmentation** — Behavior-based customer grouping (Recency, Frequency, Monetary)

✔ **At-Risk Revenue Quantification** — **$3.56M** identified at >40% churn probability

✔ **Scenario Planning** — Real-time ROI modeling ("Retain 15% of at-risk customers → save **$0.53M**")

✔ **Prioritized Action List** — **Top 50** high-risk customers ranked by revenue exposure

✔ **Behavioral Drivers** — RFM context enables targeted retention tactics per customer

---

# 📊 Dashboard Showcase

## 🎯 Page 1: RFM Segmentation Overview (Cohort Retention Matrix)

<p align="center">
  <img src="https://raw.githubusercontent.com/ThomasAldo/Subscription-Churn-Cohort-Retention-Analysis/main/docs/dashboard_page1_cohort_retention_matrix.png" width="900" alt="Cohort Retention Matrix - Historical Subscription Behavior"/>
</p>

**What it shows:**
- **Cohort-based retention tracking** across 28 months (Jan 2015–Mar 2017)
- Historical subscription behavior by cohort month
- Retention rates at each month offset (0–19 months)
- Cyclical patterns at months 3, 6, 12 (quarterly/annual renewal spikes)
- **Key Insight:** Avg 87.16% retention with strong quarterly/annual renewal dependency

**Business Value:**
- Validates churn probability model against observed cohort behavior
- Confirms retention patterns tied to billing cycles
- Identifies strategic renewal windows for intervention

---

## 🚨 Page 2: Churn Risk & At-Risk Revenue (Scenario Planning)

<p align="center">
  <img src="https://raw.githubusercontent.com/ThomasAldo/Subscription-Churn-Cohort-Retention-Analysis/main/docs/dashboard_page2_churn_risk_exposure.png" width="900" alt="Churn Risk & At-Risk Revenue Dashboard"/>
</p>

**Key Metrics:**
- **High-Risk Customers:** 1,436 (2.39% of 60K base)
- **At-Risk Revenue:** $3.56M (from high-risk segment)
- **Projected Revenue Saved (15% scenario):** $0.53M
- **Retention Success Slider:** 15% (configurable for what-if analysis)

**Interactive Elements:**

1. **Churn Probability Distribution** — Histogram showing model output; clean separation at 0.40 threshold
   - Peaks: 0.0–0.1 (low risk) and 0.7–1.0 (high risk)
   - Decision boundary: >0.40 = High Risk classification

2. **Customer Mix by Churn Risk** — Donut chart
   - 97.61% Low/Medium Risk (blue)
   - 2.39% High Risk (dark blue)

3. **Revenue Exposure by Churn Risk** — Bar chart
   - Low/Medium Risk: $134.43M (stable base)
   - High Risk: $3.56M (at-risk exposure)

4. **Scenario Planning Slider** — Real-time what-if modeling
   - Formula: At-Risk Revenue × Retention Success % = Projected Savings
   - Example: 15% retention → $0.53M saved; 50% → $1.78M

**Executive Insights:**
- High-Risk segment is small but material (2.39% of customers = 2.6% of revenue)
- Scenario planning supports ROI justification for retention initiatives
- Churn probability distribution validates model—clear separation at 0.40 threshold

---

## 🎯 Page 3: Retention Action List & Conclusion

<p align="center">
  <img src="https://raw.githubusercontent.com/ThomasAldo/Subscription-Churn-Cohort-Retention-Analysis/main/docs/dashboard_page3_action_list_conclusion.png" width="900" alt="Top 50 High-Risk Customers & Retention Strategy"/>
</p>

**Execution List:**
- **Top 50 High-Risk customers** ranked by Monetary (highest revenue exposure first)
- Columns:
  - **Customer Key** — Hashed identifier (readable format: Cust-vZEjs=, etc.)
  - **Monetary ($)** — Total customer spend (Jan 2015–Mar 2017)
  - **Churn Probability** — Model prediction (0–1 scale)
  - **Recency** — Days since last transaction
  - **Frequency** — Number of transactions
  - **RFM_Segment** — Behavioral code (e.g., 114, 124, 314, 414)

**Key Insight Box:**
- "A small High-Risk cohort drives meaningful revenue exposure. Prioritizing retention on highest-value customers maximizes expected savings and makes intervention measurable."

**What this page shows:**
- The table is the execution list: Top 50 High-Risk customers (>40% churn probability) ranked by Monetary (highest exposure first)
- Drill-down capability enables targeted outreach strategies per customer

**Summary of Findings (3-page recap):**

- **Page 1 (Cohort Matrix):** Validates churn model with historical subscription retention patterns (87.16% avg, cyclical spikes at renewals)
- **Page 2 (Risk + Exposure):** High-Risk customers small (~1.4K; 2.39%) but represent $3.56M at risk; scenario planning estimates savings (15% → $0.53M)
- **Page 3 (Action List):** Converts insights into prioritized retention plan (Top 50 by Monetary + RFM context)

**Next Actions (Recommended):**

1. **Execute outreach in priority order** (Top 50 by Monetary), starting with highest Churn Probability within top spenders
2. **Tailor retention tactics using RFM behavior:**
   - High Recency + Low Frequency → Reactivation / win-back offer
   - Low Recency + High Frequency → Service recovery / relationship outreach
   - High Monetary (any risk) → Escalate to account management team
3. **Track outcomes and iterate:**
   - Measure retention rate and revenue retained vs. baseline
   - Review 0.40 threshold and segment performance to refine targeting
   - Update model with pilot campaign results

---

# 📈 Key Findings

| Metric | Value | Impact |
|--------|-------|--------|
| **High-Risk Customers** | 1,436 | 2.39% of 60K base |
| **At-Risk Revenue** | $3.56M | 2.6% of total, but >40% churn probability |
| **Stable Revenue** | $134.43M | 97.61% customers, low/medium risk |
| **Scenario Savings (15% retention)** | $0.53M | Conservative, direct ROI |
| **Scenario Savings (50% retention)** | $1.78M | Optimistic upper-bound |
| **Data Window** | Jan 2015–Mar 2017 | 27 months of subscription history |
| **Total Transactions** | 1,003,025 | Raw transaction-level data |
| **Unique Customers** | 60,000 | RFM segmentation granularity |
| **Avg Retention Rate** | 87.16% | Historical cohort average |

---

# 🛠 Technology Stack

## 👨‍💻 Data Processing
- **Python** — ETL pipeline, data cleaning, aggregation
- **Pandas** — DataFrame manipulation, RFM calculation
- **NumPy** — Numerical operations
- **Scikit-Learn** — Churn probability model training

## 📓 Notebooks
- **Jupyter Notebook** — Data exploration, RFM calculation, model development

## 🗄 Database / Data Management
- **CSV-based** — Lightweight, portable data storage
- **Data Period:** Jan 2015–Mar 2017 (27-month snapshot)
- **Granularity:** Transaction-level (1.003M rows) → Customer-level (60K RFM output)

## 📊 Visualization & BI
- **Power BI** — Interactive dashboard (3 pages + 1 cohort validation matrix)
- **Features:** KPI cards, drill-down tables, scenario sliders, multi-chart visuals, dynamic filtering

## ⚙ Version Control
- **Git + GitHub** — Code versioning, collaboration, reproducibility

---

# 🔄 Project Workflow

```
┌──────────────────────────────┐
│  Raw Transaction Data        │ 
│  (1,003,025 rows)            │
│  portfolio_subscription_      │
│  master.csv                  │
└──────────────────────────────┘
           ↓
┌──────────────────────────────┐
│  Data Cleaning & ETL         │ 
│  (Python + Pandas)           │
│  data_process.ipynb          │
└──────────────────────────────┘
           ↓
┌──────────────────────────────┐
│  RFM Segmentation + Churn    │ 
│  Probability Model           │
│  rfm_modeling.py             │
└──────────────────────────────┘
           ↓
┌──────────────────────────────┐
│  Customer-Level RFM Output   │ 
│  (60,000 rows, 1 per cust)   │
│  rfm_segmentation_output.csv │
└──────────────────────────────┘
           ↓
┌──────────────────────────────┐
│  Power BI Dashboard          │ 
│  (3 Pages + 1 Cohort Matrix) │
│  Sub_latest.pbix             │
└──────────────────────────────┘
           ↓
┌──────────────────────────────┐
│  Business Insights & Action  │
│  Prioritized Retention Plan  │
└──────────────────────────────┘
```

---

# 📂 Project Structure

```
Subscription-Churn-Cohort-Retention-Analysis/
│
├── 📊 dashboards/
│   └── Sub_latest.pbix                          ← Power BI Dashboard (3 pages + cohort matrix)
│
├── 📁 data/
│   ├── rfm_segmentation_output.csv               ← Customer RFM + risk (60,000 rows)
│   └── sql_cohort_retention_output.csv           ← Cohort retention matrix (validation)
│
├── 📓 notebooks/
│   └── data_process.ipynb                        ← ETL & data cleaning pipeline
│
├── 🐍 scripts/
│   └── rfm_modeling.py                           ← RFM calculation + churn model
│
├── 📖 docs/
│   ├── dashboard_page1_cohort_retention_matrix.png       ← Cohort validation visual
│   ├── dashboard_page2_churn_risk_exposure.png           ← Risk quantification visual
│   ├── dashboard_page3_action_list_conclusion.png        ← Action list visual
│   ├── DATA_DICTIONARY.md                                ← Field-level documentation
│   ├── METHODOLOGY.md                                    ← RFM + modeling approach
│   └── insights_recommendations.md                       ← Executive summary
│
├── 📄 README.md                                  ← This file
├── requirements.txt                             ← Python dependencies
└── .gitignore                                   ← Git exclusions
```

---

# 📊 Methodology: RFM + Churn Prediction

## RFM Framework

| Metric | Definition | Range | Interpretation |
|--------|-----------|-------|-----------------|
| **Recency (R)** | Days since last transaction | 0–500+ | Lower = more recent = higher engagement |
| **Frequency (F)** | Number of transactions | 1–500+ | Higher = more loyal, repeat buyer |
| **Monetary (M)** | Total spend (Jan 2015–Mar 2017) | $0–$10K+ | Higher = more valuable customer |

Each metric scored **1–9** (1=worst performer, 9=best performer), creating 3-digit segment codes.

**Example Segments:**
- **114:** High recency (recent), low frequency (rare buyer), low value
- **314:** Low recency (lapsed), low frequency, high value → **WIN-BACK target**
- **414:** Low recency, moderate frequency, high value → **RELATIONSHIP RECOVERY target**

## Churn Probability Model

**Input Features:**
- RFM metrics (Recency, Frequency, Monetary)
- Behavioral flags (is_auto_renew, is_cancel)
- Subscription status (days to expiration)

**Output:**
- Churn probability: 0–1 scale (0=very likely to stay, 1=very likely to churn)

**Risk Threshold:** >0.40 = **High Risk**

**Validation:**
- Churn probability distribution shows clean separation at 0.40 threshold
- Cohort retention matrix confirms model aligns with observed churn behavior (87.16% avg retention)
- Cyclical patterns at months 3, 6, 12 align with quarterly/annual renewal windows

---

# 🎯 Business Questions Answered

✔ **Which customers are most likely to churn?**
→ High-Risk segment: 1,436 customers with >40% churn probability

✔ **What is the financial impact of churn?**
→ $3.56M revenue at risk from high-risk cohort

✔ **How much revenue can we save with intervention?**
→ Scenario planning: 15% success = $0.53M saved; 50% = $1.78M

✔ **Who should we target first?**
→ Top 50 list ranked by revenue exposure (highest Monetary first)

✔ **What retention tactic fits each customer?**
→ RFM context enables targeted plays (win-back, relationship recovery, account escalation)

✔ **Does the model align with observed behavior?**
→ Cohort matrix validates: 87.16% avg retention with cyclical spikes at renewal windows

---

# 💡 Business Impact

## 🎓 For Retention Teams
- Prioritized action list (Top 50) focuses effort on highest ROI targets
- Behavioral context (RFM) enables personalized outreach
- Scenario planning justifies budget/investment

## 💼 For Executive Leadership
- Clear quantification of churn exposure ($3.56M)
- Projected ROI of retention initiatives (up to $1.78M potential)
- Data-driven decision support with validation via cohort analysis

## 🏢 For Business Development
- Identifies churn patterns tied to renewal cycles
- Enables proactive customer success interventions at critical touchpoints
- Supports retention-focused product roadmap priorities

---

# ▶ How To Run This Project

## 1️⃣ Clone Repository
```bash
git clone https://github.com/ThomasAldo/Subscription-Churn-Cohort-Retention-Analysis.git
cd Subscription-Churn-Cohort-Retention-Analysis
```

## 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
**Required packages:**
- pandas
- numpy
- scikit-learn
- jupyter

## 3️⃣ Run Data Processing Pipeline
```bash
jupyter notebook notebooks/data_process.ipynb
```
- Cleans raw transaction data
- Aggregates to customer level
- Calculates RFM metrics
- Outputs intermediate tables

## 4️⃣ Generate RFM Segmentation & Churn Model
```bash
python scripts/rfm_modeling.py
```
- Calculates Recency, Frequency, Monetary per customer
- Trains churn probability model
- Outputs: `rfm_segmentation_output.csv`

## 5️⃣ Load Dashboard in Power BI
```
Open: dashboards/Sub_latest.pbix
Data source: data/rfm_segmentation_output.csv
```
- Auto-connects to CSV
- Refreshes on file update
- 4 interactive pages ready (3 main + 1 cohort validation matrix)

---

# 📊 Dashboard Design Highlights

✔ **Interactive Filters** — Risk level, customer segment, RFM slicing

✔ **KPI Cards** — High-risk count, at-risk revenue, projected savings

✔ **Scenario Slider** — Real-time what-if retention success modeling

✔ **Multi-Page Navigation** — Cohort Validation → Risk Quantification → Action

✔ **Drill-Down Capability** — Top 50 customers with full RFM context + behavioral codes

✔ **Distribution Validation** — Churn probability histogram + 0.40 threshold visualization

✔ **Cohort Matrix Integration** — Historical retention patterns validate model accuracy

✔ **Revenue Mix Visuals** — Donut + bar charts for risk exposure breakdown

---

# 🚀 Future Enhancements

🔮 **Time-Series Trend Analysis** — Track high-risk customer count & at-risk revenue month-over-month

🔮 **Behavioral Flags Integration** — Add `is_cancel`, `is_auto_renew`, expiration proximity columns to action list

🔮 **Holdout Model Validation** — Measure prediction accuracy (precision/recall) on unseen test set

🔮 **Pilot Campaign Tracking** — A/B test retention tactics, measure lift vs. control group

🔮 **Monthly Model Refresh** — Automated retraining on new transaction data

🔮 **Customer Lifetime Value (CLV)** — Segment high-risk customers by CLV for prioritization

🔮 **Predictive Churn Alert System** — Real-time notification when customer crosses 0.40 threshold

🔮 **Renewal Window Targeting** — Identify optimal intervention timing based on subscription expiration

---

# 📥 Dataset Information

**Data Source:** Subscription transaction history (27-month historical sample)

**Volume:** 
- 1,003,025 transaction rows
- 60,000 unique customers
- 27-month period (Jan 2015–Mar 2017)

**Data Files Available:**
- Processed RFM output: `data/rfm_segmentation_output.csv` (60K rows, customer-level)
- Cohort matrix: `data/sql_cohort_retention_output.csv` (28 cohorts × 20 months)

**Note:** Raw master dataset (portfolio_subscription_master.csv) excluded due to GitHub size limits but available upon request.

**Privacy:** Customer IDs are hashed for confidentiality.

---

# 📌 Key Metrics Reference

| KPI | Value | Context |
|-----|-------|---------|
| Total Customers | 60,000 | Unique subscribers in analysis window |
| High-Risk Customers | 1,436 | Churn probability >0.40 |
| Low/Medium Risk Customers | 58,564 | Stable, lower churn likelihood |
| At-Risk Revenue | $3.56M | High-risk segment total spend |
| Stable Revenue | $134.43M | Low/Medium risk segment |
| % High-Risk | 2.39% | Concentration in small cohort |
| Avg Retention Rate | 87.16% | Historical cohort average |
| Projected Savings (15% retention) | $0.53M | Conservative scenario |
| Projected Savings (50% retention) | $1.78M | Optimistic scenario |
| Data Period | Jan 2015–Mar 2017 | 27-month snapshot |
| Monetary Window | Full Dataset Period | Total customer spend across entire window |

---

# 📖 Documentation

For detailed technical documentation, see:
- **[DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md)** — Column-level field definitions
- **[METHODOLOGY.md](docs/METHODOLOGY.md)** — RFM calculation & churn model approach
- **[insights_recommendations.md](docs/insights_recommendations.md)** — Executive summary & next steps

---

# 👨‍💻 Author

## Thomas Aldo
### Computer Science Engineer | Data Analyst

Passionate about transforming data into actionable business insights. Specialized in **predictive analytics**, **customer retention strategy**, and **data-driven decision-making**.

### 📧 Email
thomasaldo.official@gmail.com

### 🔗 LinkedIn
[Thomas Aldo](https://www.linkedin.com/in/thomas-aldo-88a006237?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)

### 🔗 GitHub
[ThomasAldo](https://github.com/ThomasAldo)

---

## ⭐ Key Achievements

✔ **End-to-End Analytics Pipeline** — Raw data → predictive model → interactive dashboard

✔ **Business Intelligence Storytelling** — Translates technical metrics into business impact

✔ **RFM + Churn Modeling** — Production-ready predictive segmentation with historical validation

✔ **Portfolio-Ready Project** — Professional structure, documentation, reproducibility

✔ **Scenario Planning** — Real-time ROI modeling for executive decision support

---

# 📜 License

This project is developed for **educational and portfolio demonstration purposes**.

---

<p align="center"> 
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FF6B6B,50:EE5A6F,100:C92A2A&height=120&section=footer"/> 
</p>

<p align="center">
  <b>⭐ If you found this project valuable, consider starring the repository!</b>
</p>

---
