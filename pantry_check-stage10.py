# === Stage 10: Текстовый поиск ===
# Project: PantryCheck
def highlight_matches(text, needle):
    """Подсветить все вхождения needle в text, сохранив регистр исходного текста."""
    if not needle:
        return text
    result = []
    needle = needle.casefold()
    text = text.casefold()
    start = 0
    index = text.find(needle, start)
    while index != -1:
        result.append(text[start:index])
        result.append(needle)
        start = index + len(needle)
        index = text.find(needle, start)
    result.append(text[start:])
    return ''.join(result)


def build_search_query(products, needle):
    """Собрать строку вывода с подсветкой совпадений по текстовым полям продукта."""
    if not needle:
        return ""
    lines = []
    for product in products:
        name = product.get("name", "")
        category = product.get("category", "")
        if needle.casefold() in name.casefold() or needle.casefold() in category.casefold():
            name_view = highlight_matches(name, needle)
            category_view = highlight_matches(category, needle)
            lines.append(f"{name_view} [{category_view}]")
    return "\n".join(lines)


if __name__ == "__main__":
    demo = [
        {"name": "Молоко", "category": "Молочные"},
        {"name": "Хлеб", "category": "Выпечка"},
        {"name": "Молоко светлое", "category": "Молочные"},
    ]
    query = build_search_query(demo, "молоко")
    print(query)
