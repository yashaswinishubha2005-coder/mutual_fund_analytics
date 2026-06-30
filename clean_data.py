import pandas as pd
import os

# ==========================================================
# Paths
# ==========================================================
RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

# ==========================================================
# 01. fund_master.csv
# ==========================================================

df = pd.read_csv(f"{RAW_PATH}/01_fund_master.csv")

df = df.drop_duplicates()
df.columns = df.columns.str.strip()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip()

if "amfi_code" in df.columns:
    df = df.dropna(subset=["amfi_code"])

df.to_csv(f"{PROCESSED_PATH}/01_fund_master_clean.csv", index=False)

print("01 cleaned")

# ==========================================================
# 02. nav_history.csv
# ==========================================================

import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")
print("Original Shape:", df.shape)

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["amfi_code", "date"])

df = df.drop_duplicates()
df["nav"] = df.groupby("amfi_code")["nav"].ffill()


df = df[df["nav"] > 0]
print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("Cleaned file saved successfully!")


# ==========================================================
# 03. aum_by_fund_house.csv
# ==========================================================

df = pd.read_csv(f"{RAW_PATH}/03_aum_by_fund_house.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.drop_duplicates()

df = df[df["aum_crore"] > 0]

df.to_csv(f"{PROCESSED_PATH}/03_aum_by_fund_house_clean.csv", index=False)

print("03 cleaned")

# ==========================================================
# 04. monthly_sip_inflows.csv
# ==========================================================

df = pd.read_csv(f"{RAW_PATH}/04_monthly_sip_inflows.csv")

df["month"] = pd.to_datetime(df["month"])

df = df.drop_duplicates()

numeric_cols = [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore",
    "yoy_growth_pct"
]

for c in numeric_cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

df.to_csv(f"{PROCESSED_PATH}/04_monthly_sip_inflows_clean.csv", index=False)

print("04 cleaned")

# ==========================================================
# 05. category_inflows.csv
# ==========================================================

df = pd.read_csv(f"{RAW_PATH}/05_category_inflows.csv")

df["month"] = pd.to_datetime(df["month"])

df = df.drop_duplicates()

df["net_inflow_crore"] = pd.to_numeric(
    df["net_inflow_crore"],
    errors="coerce"
)

df.to_csv(f"{PROCESSED_PATH}/05_category_inflows_clean.csv", index=False)

print("05 cleaned")

# ==========================================================
# 06. industry_folio_count.csv
# ==========================================================

df = pd.read_csv(f"{RAW_PATH}/06_industry_folio_count.csv")

df["month"] = pd.to_datetime(df["month"])

df = df.drop_duplicates()

cols = [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]

for c in cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

df.to_csv(f"{PROCESSED_PATH}/06_industry_folio_count_clean.csv", index=False)

print("06 cleaned")

# ==========================================================
# 07. scheme_performance.csv
# ==========================================================

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nMissing Values:")
print(df[numeric_cols].isnull().sum())

anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(len(anomalies))

if len(anomalies) > 0:
    print(anomalies[
        ["scheme_name", "expense_ratio_pct"]
    ])


duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

print("\nCleaned Shape:", df.shape)

df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print(
    "\n07_scheme_performance_clean.csv saved successfully!"
)

# ==========================================================
# 08. investor_transactions.csv
# ==========================================================


df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

print("\nTransaction Types:")
print(df["transaction_type"].unique())

valid_types = ["Sip", "Lumpsum", "Redemption"]
df = df[df["transaction_type"].isin(valid_types)]

df["amount_inr"] = pd.to_numeric(
    df["amount_inr"],
    errors="coerce"
)

df = df[df["amount_inr"] > 0]

df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.title()
)

print("\nKYC Status Values:")
print(df["kyc_status"].unique())

valid_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("\nInvalid KYC Records:", len(invalid_kyc))

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nCleaned Shape:", df.shape)

df.to_csv(
     "data/processed/08_investor_transactions_clean.csv",
     index=False
)

print(
     "\n08_investor_transactions_clean.csv saved successfully!"
)

# ==========================================================
# 09. portfolio_holdings.csv
# ==========================================================

df = pd.read_csv(f"{RAW_PATH}/09_portfolio_holdings.csv")

df["portfolio_date"] = pd.to_datetime(df["portfolio_date"])

df = df.drop_duplicates()

df["weight_pct"] = pd.to_numeric(
    df["weight_pct"],
    errors="coerce"
)

df = df[
    df["weight_pct"].between(0,100)
]

df.to_csv(f"{PROCESSED_PATH}/09_portfolio_holdings_clean.csv", index=False)

print("09 cleaned")

# ==========================================================
# 10. benchmark_indices.csv
# ==========================================================

df = pd.read_csv(f"{RAW_PATH}/10_benchmark_indices.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.drop_duplicates()

df["close_value"] = pd.to_numeric(
    df["close_value"],
    errors="coerce"
)

df = df[df["close_value"] > 0]

df.to_csv(f"{PROCESSED_PATH}/10_benchmark_indices_clean.csv", index=False)

print("10 cleaned")

print("\nAll datasets cleaned successfully!")