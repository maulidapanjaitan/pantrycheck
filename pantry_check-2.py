# === Stage 2: Проверка полей ===
# Project: PantryCheck
import datetime


class ProductError(Exception):
    pass


def normalize_input(value):
    if value is None:
        raise ProductError("Введите значение")
    text = str(value).strip()
    if len(text) == 0:
        raise ProductError("Поле не может быть пустым")
    return text


def validate_product(product):
    if not isinstance(product, dict):
        raise ProductError("Продукт должен быть словарём")

    name = normalize_input(product.get("название"))
    if len(name) > 200:
        raise ProductError("Название слишком длинное (максимум 200 символов)")

    category = normalize_input(product.get("категория"))
    if len(category) > 100:
        raise ProductError("Категория слишком длинная (максимум 100 символов)")

    if not isinstance(product.get("количество"), (int, float)):
        raise ProductError("Количество должно быть числом")

    quantity = float(product["количество"])
    if quantity < 0:
        raise ProductError("Количество не может быть отрицательным")
    if quantity != int(quantity):
        raise ProductError("Количество должно быть целым числом")

    try:
        expiry = datetime.date.fromisoformat(str(product.get("срок годности")).strip())
    except (ValueError, TypeError):
        raise ProductError("Срок годности должен быть датой в формате ГГГГ-ММ-ДД")

    if expiry < datetime.date.today():
        raise ProductError("Срок годности уже истёк")

    product["название"] = name
    product["категория"] = category
    product["количество"] = int(quantity)
    product["срок годности"] = expiry
    return product
