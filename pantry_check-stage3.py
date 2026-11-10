# === Stage 3: Хранилище в памяти ===
# Project: PantryCheck
"""
Модуль PantryCheck: хранилище продуктов в памяти.

Предоставляет класс Product для описания единицы товара и класс
PantryStore для хранения списка продуктов с операциями добавления,
поиска по идентификатору и получения полного списка.

Используются только возможности стандартной библиотеки.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Product:
    name: str
    category: str
    quantity: float
    expiry_date: Optional[str] = None
    id: Optional[str] = None

    def __post_init__(self) -> None:
        if self.id is None:
            self.id = str(len(self.__class__._counter) + 1)
            self.__class__._counter += 1

    def is_expired(self) -> bool:
        if self.expiry_date is None:
            return False
        from datetime import date

        today = date.today().isoformat()
        return self.expiry_date < today


class PantryStore:
    """Память для продуктов кладовой."""

    _counter: int = 0

    def __init__(self) -> None:
        self._products: Dict[str, Product] = {}

    def add(self, product: Product) -> Product:
        self._products[product.id] = product
        return product

    def get(self, product_id: str) -> Optional[Product]:
        return self._products.get(product_id)

    def list_products(self) -> List[Product]:
        return list(self._products.values())

    def __len__(self) -> int:
        return len(self._products)
