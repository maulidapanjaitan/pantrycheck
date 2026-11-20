# === Stage 9: Фильтрация записей ===
# Project: PantryCheck
from datetime import date, datetime


def _parse_date(value):
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, str):
        return datetime.strptime(value.strip(), "%Y-%m-%d").date()
    return value


def filter_products(products, category=None, date_range=None):
    filtered = []
    for product in products:
        if category is not None and product.get("category") != category:
            continue
        if date_range is not None:
            product_date = _parse_date(product.get("expiry_date"))
            if product_date is None:
                continue
            if date_range.get("start") is not None and product_date < date_range["start"]:
                continue
            if date_range.get("end") is not None and product_date > date_range["end"]:
                continue
        filtered.append(product)
    return filtered


def filter_products_by_category(products, category):
    return [product for product in products if product.get("category") == category]


def filter_products_by_date(products, start=None, end=None):
    filtered = []
    for product in products:
        product_date = _parse_date(product.get("expiry_date"))
        if product_date is None:
            continue
        if start is not None and product_date < start:
            continue
        if end is not None and product_date > end:
            continue
        filtered.append(product)
    return filtered


def filter_products_by_category_and_date(products, category, start=None, end=None):
    return [
        product
        for product in filter_products_by_category(products, category)
        if _parse_date(product.get("expiry_date")) is not None
        and (start is None or _parse_date(product.get("expiry_date")) >= start)
        and (end is None or _parse_date(product.get("expiry_date")) <= end)
    ]
