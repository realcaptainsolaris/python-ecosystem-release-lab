"""Smoke test for NumPy on Python 3.15."""

import platform
import sys

import numpy as np


def main() -> None:
    """Run a small set of representative NumPy operations."""
    print("NumPy / Python 3.15 compatibility test")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"NumPy: {np.__version__}")

    values = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
        ]
    )

    normalized = (values - values.mean(axis=0)) / values.std(axis=0)

    weights = np.array([0.5, 1.0, 1.5])
    scores = normalized @ weights

    print(f"Shape: {values.shape}")
    print(f"Column means: {values.mean(axis=0)}")
    print(f"Normalized:\n{normalized}")
    print(f"Scores: {scores}")
    print("Result: OK")


if __name__ == "__main__":
    main()
