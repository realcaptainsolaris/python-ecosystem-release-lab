"""Smoke test for Polars on Python 3.15."""

import platform
import sys

import polars as pl


def main() -> None:
    """Run representative eager and lazy Polars operations."""
    print("Polars / Python 3.15 compatibility test")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"Polars: {pl.__version__}")

    df = pl.DataFrame(
        {
            "category": ["A", "B", "A", "B", "A"],
            "value": [10.0, 20.0, None, 40.0, 50.0],
            "quantity": [1, 2, 3, 1, 2],
        }
    )

    result = (
        df.lazy()
        .with_columns(
            pl.col("value").fill_null(pl.col("value").median()),
        )
        .with_columns(
            (pl.col("value") * pl.col("quantity")).alias("total"),
        )
        .group_by("category")
        .agg(
            pl.col("total").sum(),
            pl.col("value").mean().alias("average"),
            pl.len().alias("rows"),
        )
        .sort("category")
        .collect()
    )

    print(f"Shape: {df.shape}")
    print(f"Null values: {df.null_count().sum_horizontal()[0]}")
    print(f"LazyFrame result:\n{result}")
    print("Result: OK")


if __name__ == "__main__":
    main()
