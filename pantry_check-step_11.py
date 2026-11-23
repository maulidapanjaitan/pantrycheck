# === Stage 11: Теги ===
# Project: PantryCheck
from datetime import date


class ProductTag:
    def __init__(self, name):
        self.name = name


def add_tag(products, product_name, tag_name):
    for product in products:
        if product["name"] == product_name:
            if tag_name not in product["tags"]:
                product["tags"].append(tag_name)
            return True
    return False


def remove_tag(products, product_name, tag_name):
    for product in products:
        if product["name"] == product_name:
            if tag_name in product["tags"]:
                product["tags"].remove(tag_name)
            return True
    return False


def search_by_tag(products, tag_name):
    return [product for product in products if tag_name in product["tags"]]
