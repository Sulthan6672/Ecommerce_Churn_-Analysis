import pandas as pd
from pymongo import MongoClient

# Establish a secure data bridge with your local MongoDB instance
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["EcommerceDB"]
    collection = db["customers"]
    
    # Extract live raw documents out of the cluster collections
    df = pd.DataFrame(list(collection.find()))
    print("✅ Live Data Layer Handshake Established with MongoDB!")
except Exception as e:
    print(f"❌ Connection Blocked: {e}")
    exit()

# Run advanced cohort risk logic
total_users = len(df)
no_discount_churners = len(df[(df['Discount_Used'] == 'No') & (df['Churn'] == 'Yes')])
no_discount_total_base = len(df[df['Discount_Used'] == 'No'])
calculated_risk_ratio = (no_discount_churners / no_discount_total_base) * 100

print("\n==================================================")
print("       MONGODB DATA STREAM PIPELINE REPORT        ")
print("==================================================")
print(f"Total Portfolio Profiles Checked : {total_users}")
print(f"No-Discount Cohort Churn Velocity: {calculated_risk_ratio:.1f}%")
print("==================================================")

# Target list compilation: Find buyers sitting at extreme risk windows
# Filter condition: No discount usage, not yet churned, high inactive day lag
extreme_risk_segment = df[(df['Discount_Used'] == 'No') & (df['Churn'] == 'No') & (df['Last_Purchase_Days_Ago'] > 60)]

# Write targeting file directly back to marketing team directories
extreme_risk_segment[['Customer_ID', 'Location', 'Total_Spend', 'Last_Purchase_Days_Ago']].to_csv("targeted_retention_list.csv", index=False)
print("💾 Live target matrix successfully compiled into 'targeted_retention_list.csv'!")