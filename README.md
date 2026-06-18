# E-Commerce Customer Retention & Churn Control

This repository houses an end-to-end analytics and data pipeline infrastructure focused on identifying, analyzing, and mitigating customer churn for an E-Commerce platform. By coupling a relational and modern NoSQL database data layer with an automated data pipeline, the project transforms raw customer transactions into production-ready analytical dashboards and actionable high-risk target sheets for proactive marketing outreach.

---

## 📊 Live Interactive Dashboard

You can explore the fully interactive analytical control center directly on Tableau Public:

👉 **[View the E-Commerce Customer Retention & Churn Control Center](https://public.tableau.com/views/Book1_17815246077530/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

---

## 🛠️ Project Architecture & Data Flow

The project is structured into three primary operational layers:

```
┌─────────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│     MongoDB Layer       │ ───> │  Python ETL & Analytics │ ───> │ Tableau Business Intel  │
│  (Raw Customer Profiles)│      │   (Cohort Risk Scripts) │      │ (Control Center Visuals)│
└─────────────────────────┘      └─────────────────────────┘      └─────────────────────────┘
                                              │                                │
                                              ▼                                ▼
                                 Actionable Target Matrix          Executive Insights
                                 • targeted_retention_list.csv    • The Churn Overview Graph
                                 • mongo_winback_list.csv         • The Revenue Exposure Graph
```

1. **The MongoDB Data Layer (`EcommerceDB.customers`):** Acts as the localized cluster dataset containing transactional history, app analytics, customer service records, and demographics.
2. **Python Data Engine:** Establishes a secure data bridge pipeline to live extract collections from the MongoDB cluster, run predictive/cohort logic using `pandas`, and output highly granular, filter-specific campaign spreadsheets directly back to growth marketing teams.
3. **Tableau Business Intelligence Hub:** Consumes structured data (`Ecommerce_Customer_Churn_Pivot_Table.xlsx`) to spin up an executive monitoring dashboard, tracks behavioral indicators, and monitors regional revenue exposure.

---

## 📂 Core Repository Structure

* **`mongo_winback_list.csv`**: A structured analytical output matrix targeting historically churned profiles from the MongoDB environment that require strategic promotional or financial outreach to win back.
* **`targeted_retention_list.csv`**: An automatically generated active prevention directory containing buyers sitting at extreme churn windows (e.g., zero historical discount usage, active status, but an inactive duration > 60 days) to facilitate proactive retention campaigns.
* **Tableau Infrastructure Workbook (`Book1.twb`)**: A highly optimized corporate layout connecting back to the analytical pivot data sources, organizing content into:
  * *Sheet 1: The Churn Overview Graph* — Cross-tabulating customer identifiers with behavioral habits such as coupon usage to uncover underlying drop-off trends.
  * *Sheet 2: The Revenue Exposure Graph* — Geographically mapping localized absolute spending margins via interactive bubble charts to spot vulnerable markets.
  * *Dashboard 1: E-Commerce Customer Retention & Churn Control Center* — An interactive control environment featuring mobile device layouts, automated caching, and strict responsive zone mapping for multi-device analytics.

---

## 🚀 Getting Started

### 1. Data Layer Handshake (MongoDB Configuration)
Ensure your MongoDB local instance is running on port `27017` and populated under the database named `EcommerceDB` and collection `customers`.

### 2. Running the Risk Pipelines
Execute the Python data stream scripts to check portfolio profiles, compute cohort velocity metrics, and compile the actionable marketing tables:

```python
# Extract live raw documents and compute risk ratio
import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["EcommerceDB"]
collection = db["customers"]
df = pd.DataFrame(list(collection.find()))

# Filter active cohorts at risk (No historical discount, inactive for > 60 days)
extreme_risk_segment = df[(df['Discount_Used'] == 'No') & (df['Churn'] == 'No') & (df['Last_Purchase_Days_Ago'] > 60)]
extreme_risk_segment[['Customer_ID', 'Location', 'Total_Spend', 'Last_Purchase_Days_Ago']].to_csv("targeted_retention_list.csv", index=False)
```

---

## 📊 Business Intelligence & Key Dashboards

The Tableau workbook translates transactional data into business intelligence via the **E-Commerce Customer Retention & Churn Control Center**:
* **The Churn Overview:** Visualizes behavioral drop-offs, isolating cohorts with lower application usage hours and high customer service inquiries.
* **The Revenue Exposure:** Dynamically evaluates absolute financial exposure. Larger visual clusters indicate major target regions requiring immediate churn intervention to shield the platform's bottom line.
