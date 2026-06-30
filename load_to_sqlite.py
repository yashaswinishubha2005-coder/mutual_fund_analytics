from sqlalchemy import create_engine
import pandas as pd

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# ===========================
# Load Fund Master
# ===========================
fund = pd.read_csv("data/processed/01_fund_master_clean.csv")
fund.to_sql("dim_fund", engine, if_exists="replace", index=False)

# ===========================
# Load NAV History
# ===========================
nav = pd.read_csv("data/processed/02_nav_history_clean.csv")
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

# ===========================
# Load AUM
# ===========================
aum = pd.read_csv("data/processed/03_aum_by_fund_house_clean.csv")
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

# ===========================
# Load Monthly SIP Inflows
# ===========================
sip = pd.read_csv("data/processed/04_monthly_sip_inflows_clean.csv")
sip.to_sql("fact_sip", engine, if_exists="replace", index=False)

# ===========================
# Load Category Inflows
# ===========================
category = pd.read_csv("data/processed/05_category_inflows_clean.csv")
category.to_sql("fact_category_inflow", engine, if_exists="replace", index=False)

# ===========================
# Load Industry Folios
# ===========================
folios = pd.read_csv("data/processed/06_industry_folio_count_clean.csv")
folios.to_sql("fact_folios", engine, if_exists="replace", index=False)

# ===========================
# Load Scheme Performance
# ===========================
performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

# ===========================
# Load Investor Transactions
# ===========================
transactions = pd.read_csv("data/processed/08_investor_transactions_clean.csv")
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)

# ===========================
# Load Portfolio Holdings
# ===========================
holdings = pd.read_csv("data/processed/09_portfolio_holdings_clean.csv")
holdings.to_sql("fact_holdings", engine, if_exists="replace", index=False)

# ===========================
# Load Benchmark Indices
# ===========================
benchmark = pd.read_csv("data/processed/10_benchmark_indices_clean.csv")
benchmark.to_sql("dim_benchmark", engine, if_exists="replace", index=False)

print("===================================")
print("Database Loaded Successfully!")
print("All cleaned datasets imported.")
print("===================================")