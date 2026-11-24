# === Stage 12: Группировка ===
# Project: PantryCheck
def group_by_category(products):
    """Группирует продукты по полю «категория».

    Возвращает список кортежей (категория, список продуктов),
    отсортированный по названию категории.
    """
    groups = {}
    for product in products:
        category = product.get("category")
        groups.setdefault(category, []).append(product)
    return sorted(groups.items(), key=lambda item: item[0])


def count_by_category(products):
    """Подсчитывает количество продуктов в каждой категории.

    Возвращает словарь {категория: количество}.
    """
    counts = {}
    for product in products:
        category = product.get("category")
        counts[category] = counts.get(category, 0) + 1
    return counts


def summarize_inventory(products):
    """Формирует сводку по категориям.

    Возвращает список кортежей
    (категория, количество, список названий продуктов) в алфавитном порядке.
    """
    summary = {}
    for product in products:
        category = product.get("category")
        name = product.get("name")
        if category not in summary:
            summary[category] = {"count": 0, "names": []}
        summary[category]["count"] += 1
        summary[category]["names"].append(name)
    return sorted(
        (category, data["count"], data["names"])
        for category, data in summary.items()
    )


def top_categories(products, limit=5):
    """Возвращает категории с наибольшим количеством продуктов.

    Параметр limit ограничивает число возвращаемых категорий.
    """
    counts = count_by_category(products)
    return sorted(counts.items(), key=lambda item: item[1], reverse=True)[:limit]


if __name__ == "__main__":
    sample = [
        {"name": "Молоко", "category": "Молочные", "quantity": 2, "expiry": "2025-12-31"},
        {"name": "Хлеб", "category": "Хлебобулочные", "quantity": 1, "expiry": "2025-12-20"},
        {"name": "Сыр", "category": "Молочные", "quantity": 3, "expiry": "2026-01-10"},
        {"name": "Яйца", "category": "Молочные", "quantity": 10, "expiry": "2026-02-01"},
        {"name": "Масло", "category": "Хлебобулочные", "quantity": 1, "expiry": "2026-01-05"},
    ]
    print("Группы:", group_by_category(sample))
    print("Подсчёт:", count_by_category(sample))
    print("Сводка:", summarize_inventory(sample))
    print("Топ:", top_categories(sample))
