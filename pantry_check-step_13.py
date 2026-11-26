# === Stage 13: Постраничный вывод ===
# Project: PantryCheck
from typing import List, Dict, Any


def paginate(
    items: List[Any],
    page: int,
    page_size: int,
) -> Dict[str, Any]:
    if page_size <= 0:
        page_size = 1
    if page < 1:
        page = 1
    total = len(items)
    total_pages = (total + page_size - 1) // page_size
    if page > total_pages:
        page = total_pages
    start = (page - 1) * page_size
    end = start + page_size
    return {
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": total_pages,
        "items": items[start:end],
    }
