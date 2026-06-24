import pandas as pd

# df = pd.read_csv("data/raw/02_nav_history.csv")
# print("Original Shape:", df.shape)

# df["date"] = pd.to_datetime(df["date"])
# df = df.sort_values(["amfi_code", "date"])

# df = df.drop_duplicates()
# df["nav"] = df.groupby("amfi_code")["nav"].ffill()


# df = df[df["nav"] > 0]
# print("Cleaned Shape:", df.shape)

# df.to_csv(
#     "data/processed/02_nav_history_clean.csv",
#     index=False
# )

# print("Cleaned file saved successfully!")

# # =====================================================
# # CLEAN INVESTOR TRANSACTIONS
# # =====================================================

# df = pd.read_csv("data/raw/08_investor_transactions.csv")

# print("Original Shape:", df.shape)

# df["transaction_date"] = pd.to_datetime(
#     df["transaction_date"],
#     errors="coerce"
# )

# df["transaction_type"] = (
#     df["transaction_type"]
#     .astype(str)
#     .str.strip()
#     .str.title()
# )

# print("\nTransaction Types:")
# print(df["transaction_type"].unique())

# valid_types = ["Sip", "Lumpsum", "Redemption"]

# df = df[df["transaction_type"].isin(valid_types)]

# df["amount_inr"] = pd.to_numeric(
#     df["amount_inr"],
#     errors="coerce"
# )

# df = df[df["amount_inr"] > 0]

# df["kyc_status"] = (
#     df["kyc_status"]
#     .astype(str)
#     .str.strip()
#     .str.title()
# )

# print("\nKYC Status Values:")
# print(df["kyc_status"].unique())

# valid_kyc = ["Verified", "Pending", "Rejected"]

# invalid_kyc = df[
#     ~df["kyc_status"].isin(valid_kyc)
# ]

# print("\nInvalid KYC Records:", len(invalid_kyc))

# duplicates = df.duplicated().sum()

# print("\nDuplicate Rows:", duplicates)

# df = df.drop_duplicates()

# print("\nMissing Values:")
# print(df.isnull().sum())

# print("\nCleaned Shape:", df.shape)

# df.to_csv(
#     "data/processed/08_investor_transactions_clean.csv",
#     index=False
# )

# print(
#     "\n08_investor_transactions_clean.csv saved successfully!"
# )
# # =====================================================
# # CLEAN SCHEME PERFORMANCE
# # =====================================================

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