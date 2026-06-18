import pandas as pd
from pymongo import MongoClient

# 1. Connect to your local MongoDB server
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["EcommerceDB"]
    collection = db["customers"]
    
    # Extract data from Mongo into a Python Pandas Dataframe
    df = pd.DataFrame(list(collection.find()))
    print("✅ Successfully pulled customer records from MongoDB Collection!\n")
except Exception as e:
    print(f"❌ Connection Failed: {e}")
    exit()

# 2. Perform the analytical logic on the live Mongo export
total_accounts = len(df)
no_discount_churn = len(df[(df['Discount_Used'] == 'No') & (df['Churn'] == 'Yes')])
no_discount_total = len(df[df['Discount_Used'] == 'No'])

churn_percentage = (no_discount_churn / no_discount_total) * 100

print("==================================================")
print("         MONGODB DATA LAYER INTEGRATION           ")
print("==================================================")
print(f"Total Database Documents Read : {total_accounts}")
print(f"No-Discount Group Churn Rate  : {churn_percentage:.1f}%")
print("==================================================")