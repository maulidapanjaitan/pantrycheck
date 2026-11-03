# === Stage 1: Каркас модуля ===
# Project: PantryCheck
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Product:
    name: str
    category: str
    quantity: int
    expiry_date: date


def create_demo_products() -> list[Product]:
    return [
        Product("Молоко", "Молочные", 5, date(2025, 1, 15)),
        Product("Хлеб", "Хлебобулочные", 3, date(2025, 1, 10)),
        Product("Яйца", "Молочные", 12, date(2025, 2, 1)),
        Product("Макароны", "Сухофрукты", 20, date(2025, 12, 31)),
        Product("Масло сливочное", "Молочные", 4, date(2025, 1, 20)),
    ]


def main() -> None:
    products = create_demo_products()
    print("ПантриЧек: инвентаризация кладовой")
    print("=" * 30)
    for product in products:
        print(
            f"- {product.name} [{product.category}]: "
            f"{product.quantity} шт., срок годности: {product.expiry_date}"
        )
    print("=" * 30)
    print(f"Всего позиций в кладовой: {len(products)}")


if __name__ == "__main__":
    main()
