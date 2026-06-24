# Data Dictionary - Mutual Fund Analytics

## dim_fund

| Column Name | Data Type | Description | Source |
|------------|------------|------------|------------|
| amfi_code | Integer | Unique AMFI Scheme Code | 01_fund_master.csv |
| scheme_name | Text | Mutual Fund Scheme Name | 01_fund_master.csv |
| fund_house | Text | Asset Management Company | 01_fund_master.csv |
| category | Text | Fund Category | 01_fund_master.csv |
| sub_category | Text | Fund Sub Category | 01_fund_master.csv |
| risk_grade | Text | Risk Classification | 01_fund_master.csv |

---

## fact_nav

| Column Name | Data Type | Description | Source |
|------------|------------|------------|------------|
| amfi_code | Integer | AMFI Scheme Code | 02_nav_history.csv |
| date | Date | NAV Date | 02_nav_history.csv |
| nav | Float | Net Asset Value | 02_nav_history.csv |

---

## fact_transactions

| Column Name | Data Type | Description | Source |
|------------|------------|------------|------------|
| investor_id | Integer | Investor Identifier | 08_investor_transactions.csv |
| transaction_date | Date | Transaction Date | 08_investor_transactions.csv |
| amfi_code | Integer | Scheme Code | 08_investor_transactions.csv |
| transaction_type | Text | SIP / Lumpsum / Redemption | 08_investor_transactions.csv |
| amount_inr | Float | Transaction Amount in INR | 08_investor_transactions.csv |
| state | Text | Investor State | 08_investor_transactions.csv |
| city | Text | Investor City | 08_investor_transactions.csv |
| city_tier | Text | City Classification | 08_investor_transactions.csv |
| age_group | Text | Investor Age Group | 08_investor_transactions.csv |
| gender | Text | Investor Gender | 08_investor_transactions.csv |
| annual_income_lakh | Float | Annual Income (Lakhs) | 08_investor_transactions.csv |
| payment_mode | Text | Mode of Payment | 08_investor_transactions.csv |
| kyc_status | Text | KYC Verification Status | 08_investor_transactions.csv |

---

## fact_performance

| Column Name | Data Type | Description | Source |
|------------|------------|------------|------------|
| amfi_code | Integer | AMFI Scheme Code | 07_scheme_performance.csv |
| return_1yr_pct | Float | 1-Year Return (%) | 07_scheme_performance.csv |
| return_3yr_pct | Float | 3-Year Return (%) | 07_scheme_performance.csv |
| return_5yr_pct | Float | 5-Year Return (%) | 07_scheme_performance.csv |
| benchmark_3yr_pct | Float | Benchmark Return (%) | 07_scheme_performance.csv |
| alpha | Float | Alpha Measure | 07_scheme_performance.csv |
| beta | Float | Beta Measure | 07_scheme_performance.csv |
| sharpe_ratio | Float | Sharpe Ratio | 07_scheme_performance.csv |
| sortino_ratio | Float | Sortino Ratio | 07_scheme_performance.csv |
| std_dev_ann_pct | Float | Annualized Standard Deviation | 07_scheme_performance.csv |
| max_drawdown_pct | Float | Maximum Drawdown (%) | 07_scheme_performance.csv |
| aum_crore | Float | Assets Under Management (Crore) | 07_scheme_performance.csv |
| expense_ratio_pct | Float | Expense Ratio (%) | 07_scheme_performance.csv |
| morningstar_rating | Integer | Morningstar Rating | 07_scheme_performance.csv |
| risk_grade | Text | Risk Classification | 07_scheme_performance.csv |