"""Smoke test for pandas on Python 3.15."""

import platform
import sys

import pandas as pd


def main() -> None:
    """Run representative pandas DataFrame operations."""
    print("pandas / Python 3.15 compatibility test")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"pandas: {pd.__version__}")

    df = pd.DataFrame(
        {
            "category": ["A", "B", "A", "B", "A"],
            "value": [10.0, 20.0, None, 40.0, 50.0],
            "quantity": [1, 2, 3, 1, 2],
        }
    )

    df["value"] = df["value"].fillna(df["value"].median())
    df["total"] = df["value"] * df["quantity"]

    summary = (
        df.groupby("category")
        .agg(
            total=("total", "sum"),
            average=("value", "mean"),
            rows=("value", "size"),
        )
        .reset_index()
    )

    print(f"Shape: {df.shape}")
    print(f"Missing values: {df.isna().sum().sum()}")
    print(f"DataFrame:\n{df}")
    print(f"GroupBy result:\n{summary}")
    print("Result: OK")


if __name__ == "__main__":
    main()
