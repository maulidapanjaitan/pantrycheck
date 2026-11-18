# === Stage 8: Генерация идентификаторов ===
# Project: PantryCheck
import uuid
from datetime import datetime


PROJECT_PREFIX = "pantry"


def generate_product_id(name: str, category: str) -> str:
    """Генерация уникального идентификатора продукта с префиксом проекта."""
    base = f"{PROJECT_PREFIX}-product-{uuid.uuid4().hex[:8]}"
    return base


def generate_movement_id(product_name: str, movement_type: str, quantity: int) -> str:
    """Генерация уникального идентификатора движения с префиксом проекта."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    base = f"{PROJECT_PREFIX}-move-{timestamp}-{uuid.uuid4().hex[:6]}"
    return base


def has_collision(existing_ids: set, new_id: str) -> bool:
    """Проверка коллизии идентификатора с уже существующими."""
    return new_id in existing_ids


def unique_id(existing_ids: set, generator, *args) -> str:
    """Генерация уникального идентификатора с проверкой коллизий."""
    new_id = generator(*args)
    if has_collision(existing_ids, new_id):
        new_id = f"{new_id}-{uuid.uuid4().hex[:4]}"
        existing_ids.add(new_id)
    else:
        existing_ids.add(new_id)
    return new_id


if __name__ == "__main__":
    existing_ids = set()
    p1 = unique_id(existing_ids, generate_product_id, "Молоко", "Молочные")
    p2 = unique_id(existing_ids, generate_product_id, "Молоко", "Молочные")
    m1 = unique_id(existing_ids, generate_movement_id, "Молоко", "purchase", 5)
    print(p1)
    print(p2)
    print(m1)
    print(has_collision(existing_ids, p1))
