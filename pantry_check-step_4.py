# === Stage 4: Редактирование записей ===
# Project: PantryCheck
ALLOWED_FIELDS = ("name", "category", "quantity", "expiry_date")


class Product:
    def __init__(self, product_id, name, category, quantity, expiry_date):
        self.id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.expiry_date = expiry_date

    def update(self, changes):
        for field in ALLOWED_FIELDS:
            if field in changes:
                setattr(self, field, changes[field])

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "expiry_date": self.expiry_date,
        }


def find_product(products, product_id):
    for product in products:
        if product.id == product_id:
            return product
    return None


def edit_product(products, product_id, changes):
    product = find_product(products, product_id)
    if product is None:
        return None, "Product not found"
    product.update(changes)
    return product, None


if __name__ == "__main__":
    sample_products = [
        Product(1, "Milk", "Dairy", 5, "2025-12-31"),
        Product(2, "Bread", "Bakery", 3, "2025-06-15"),
    ]

    print("Initial products:")
    for product in sample_products:
        print(product.to_dict())

    updated, error = edit_product(
        sample_products, 1, {"name": "Whole Milk", "quantity": 8}
    )
    if error:
        print("Error:", error)
    else:
        print("\nUpdated product:")
        print(updated.to_dict())

    updated, error = edit_product(
        sample_products, 1, {"name": "Eggs", "expiry_date": "2025-01-01"}
    )
    if error:
        print("Error:", error)
    else:
        print("\nUpdated product:")
        print(updated.to_dict())
