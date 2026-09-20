"""Smoke test for Pydantic on Python 3.15."""

import platform
import sys

import pydantic
from pydantic import BaseModel, Field, ValidationError


class Product(BaseModel):
    """Represent a validated product."""

    name: str
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


def main() -> None:
    """Run representative Pydantic validation operations."""
    print("Pydantic / Python 3.15 compatibility test")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"Pydantic: {pydantic.__version__}")

    product = Product(
        name="Python Book",
        price="39.90",
        quantity=5,
    )

    print(f"Validated model: {product}")
    print(f"Serialized model: {product.model_dump()}")

    try:
        Product(
            name="Invalid Product",
            price=-10,
            quantity=1,
        )
    except ValidationError as error:
        print(f"Invalid input rejected: {error.error_count()} validation error(s)")

    print("Result: OK")


if __name__ == "__main__":
    main()
