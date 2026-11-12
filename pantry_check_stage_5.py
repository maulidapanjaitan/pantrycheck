# === Stage 5: Удаление и восстановление ===
# Project: PantryCheck
from datetime import datetime


class Product:
    def __init__(self, name, category, quantity, expiry_date):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.expiry_date = expiry_date
        self.is_deleted = False

    def delete(self):
        self.is_deleted = True

    def restore(self):
        self.is_deleted = False

    def remove(self):
        self.is_deleted = False
        self.quantity = 0
        self.expiry_date = None

    def __repr__(self):
        if self.is_deleted:
            return f"<Product {self.name!r} DELETED>"
        return (f"<Product name={self.name!r} category={self.category!r} "
                f"quantity={self.quantity} expiry={self.expiry_date}>"
                if self.quantity > 0
                else f"<Product name={self.name!r} category={self.category!r} EMPTY>"
                if self.quantity == 0
                else f"<Product name={self.name!r} category={self.category!r} "
                     f"EXPIRED expiry={self.expiry_date}>")


class ProductRegistry:
    def __init__(self):
        self._products = {}

    def add(self, product):
        self._products[product.name] = product
        return product

    def get(self, name):
        return self._products.get(name)

    def list_products(self):
        return list(self._products.values())

    def get_active(self):
        return [p for p in self._products.values() if not p.is_deleted]

    def remove(self, name):
        product = self._products.get(name)
        if product is not None:
            product.remove()
        return product

    def __len__(self):
        return len(self._products)

    def __iter__(self):
        return iter(self._products.values())
