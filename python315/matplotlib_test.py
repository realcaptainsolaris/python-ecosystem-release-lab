"""Smoke test for Matplotlib on Python 3.15."""

import platform
import sys
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    """Render and save a Matplotlib figure."""
    print("Matplotlib / Python 3.15 compatibility test")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"Matplotlib: {matplotlib.__version__}")
    print(f"Backend: {matplotlib.get_backend()}")

    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    figure, axis = plt.subplots()
    axis.plot(x, y)
    axis.set(
        title="Matplotlib on Python 3.15",
        xlabel="x",
        ylabel="sin(x)",
    )

    output = Path("python315/matplotlib_test.png")
    figure.savefig(output)
    plt.close(figure)

    print(f"Figure written: {output}")
    print(f"File size: {output.stat().st_size} bytes")
    print("Result: OK")


if __name__ == "__main__":
    main()
