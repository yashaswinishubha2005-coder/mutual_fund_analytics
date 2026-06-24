# import pandas as pd
# import os

# data_path = "data/raw"

# csv_files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

# for file in csv_files:
#     print("\n" + "="*60)
#     print(f"FILE: {file}")
#     print("="*60)

#     df = pd.read_csv(os.path.join(data_path, file))

#     print("\nShape:")
#     print(df.shape)

#     print("\nData Types:")
#     print(df.dtypes)

#     print("\nFirst 5 Rows:")
#     print(df.head())

#     print("\nMissing Values:")
#     print(df.isnull().sum())

import pandas as pd

# fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# print("\nUnique Fund Houses:")
# print(fund_master["fund_house"].unique())

# print("\nUnique Categories:")
# print(fund_master["category"].unique())

# print("\nUnique Sub Categories:")
# print(fund_master["sub_category"].unique())

# print("\nUnique Risk Categories:")
# print(fund_master["risk_category"].unique())

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("\nMissing AMFI Codes:")
print(missing_codes)

print("Missing Count:", len(missing_codes))
if len(missing_codes) == 0:
    print("\nAll AMFI codes in fund_master exist in nav_history")
else:
    print("\nMissing AMFI Codes Found")


print("\n" + "="*60)
print("DATA QUALITY SUMMARY")
print("="*60)

print(f"Fund Master Records: {len(fund_master)}")
print(f"NAV History Records: {len(nav_history)}")

print(f"Missing values in Fund Master: {fund_master.isnull().sum().sum()}")
print(f"Missing values in NAV History: {nav_history.isnull().sum().sum()}")

print(f"Duplicate rows in Fund Master: {fund_master.duplicated().sum()}")
print(f"Duplicate rows in NAV History: {nav_history.duplicated().sum()}")

print(f"Missing AMFI Codes: {len(missing_codes)}")