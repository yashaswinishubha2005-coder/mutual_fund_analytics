
CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    risk_grade TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date DATE,
    nav REAL,
    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_id INTEGER,
    amfi_code INTEGER,
    transaction_date DATE,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    date DATE,
    aum_crore REAL
);

CREATE TABLE fact_sip (
    sip_id INTEGER PRIMARY KEY AUTOINCREMENT,
    month DATE,
    sip_inflow_crore REAL,
    active_sip_accounts_crore REAL
);

CREATE TABLE fact_category_inflow (
    inflow_id INTEGER PRIMARY KEY AUTOINCREMENT,
    month DATE,
    category TEXT,
    net_inflow_crore REAL
);

CREATE TABLE fact_holdings (
    holding_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    stock_symbol TEXT,
    sector TEXT,
    weight_pct REAL,
    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);