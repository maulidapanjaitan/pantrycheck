# === Stage 6: Связанная сущность ===
# Project: PantryCheck
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional


@dataclass
class Movement:
    product_id: int
    kind: str
    quantity: int
    note: str = ""
    when: date = field(default_factory=date.today)

    def __post_init__(self):
        if self.kind not in ("in", "out"):
            raise ValueError("kind должен быть 'in' или 'out'")
        if self.quantity <= 0:
            raise ValueError("количество должно быть положительным")

    @property
    def product_name(self):
        return self.product_id

    def summary(self) -> str:
        verb = "закупка" if self.kind == "in" else "списание"
        return f"{verb}: {self.quantity} ед. продукта {self.product_id}"


class MovementLog:
    def __init__(self):
        self._records: list[Movement] = []

    def add(self, product_id: int, kind: str, quantity: int, note: str = "") -> Movement:
        if kind not in ("in", "out"):
            raise ValueError("kind должен быть 'in' или 'out'")
        if quantity <= 0:
            raise ValueError("количество должно быть положительным")
        record = Movement(product_id=product_id, kind=kind, quantity=quantity, note=note)
        self._records.append(record)
        return record

    def get(self, product_id: int) -> list[Movement]:
        return [m for m in self._records if m.product_id == product_id]

    def total_in(self, product_id: int) -> int:
        return sum(m.quantity for m in self.get(product_id) if m.kind == "in")

    def total_out(self, product_id: int) -> int:
        return sum(m.quantity for m in self.get(product_id) if m.kind == "out")

    def recent(self, limit: int = 10) -> list[Movement]:
        return list(reversed(self._records[-limit:]))


def demo():
    log = MovementLog()
    log.add(1, "in", 10, "поставка")
    log.add(1, "out", 3, "отдал")
    log.add(2, "in", 5)
    print(log.summary())
    print("закуплено:", log.total_in(1), "списано:", log.total_out(1))
    print("последние:", log.recent(2))


if __name__ == "__main__":
    demo()
