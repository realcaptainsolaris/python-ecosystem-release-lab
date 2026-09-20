"""Smoke test for scikit-learn on Python 3.15."""

import platform
import sys

import sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    """Train and evaluate a small scikit-learn pipeline."""
    print("scikit-learn / Python 3.15 compatibility test")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"scikit-learn: {sklearn.__version__}")

    features, target = load_iris(return_X_y=True)

    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.25,
        random_state=42,
        stratify=target,
    )

    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=500),
    )

    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"Training samples: {len(x_train)}")
    print(f"Test samples: {len(x_test)}")
    print(f"Predictions: {predictions[:10]}")
    print(f"Accuracy: {accuracy:.4f}")
    print("Result: OK")


if __name__ == "__main__":
    main()
