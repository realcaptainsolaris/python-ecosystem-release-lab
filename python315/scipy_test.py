"""Smoke test for SciPy on Python 3.15."""

import platform
import sys

import scipy
from scipy.integrate import quad
from scipy.optimize import minimize_scalar


def main() -> None:
    """Run representative SciPy numerical operations."""
    print("SciPy / Python 3.15 compatibility test")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"SciPy: {scipy.__version__}")

    integral, error = quad(lambda x: x**2, 0.0, 1.0)

    optimization = minimize_scalar(
        lambda x: (x - 3.0) ** 2,
        bounds=(0.0, 10.0),
        method="bounded",
    )

    print(f"Integral of x^2 from 0 to 1: {integral:.8f}")
    print(f"Estimated integration error: {error:.2e}")
    print(f"Optimization minimum: x={optimization.x:.8f}")
    print(f"Optimization success: {optimization.success}")
    print("Result: OK")


if __name__ == "__main__":
    main()
