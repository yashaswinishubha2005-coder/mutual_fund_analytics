import pandas as pd


def recommend(risk_appetite):

    performance = pd.read_csv(
        "data/processed/07_scheme_performance_clean.csv"
    )

    risk_appetite = risk_appetite.strip().title()

    funds = performance[
        performance["risk_grade"] == risk_appetite
    ]

    funds = funds.sort_values(
        by="sharpe_ratio",
        ascending=False
    )

    return funds[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ].head(3)


def print_recommendation(risk):

    recommendations = recommend(risk)

    print("\n==============================")
    print(" FUND RECOMMENDATION")
    print("==============================")
    print(f"Risk Appetite : {risk}")
    print("==============================\n")

    print(recommendations.to_string(index=False))