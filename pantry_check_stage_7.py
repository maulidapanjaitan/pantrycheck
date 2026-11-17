# === Stage 7: Связи между сущностями ===
# Project: PantryCheck
def get_product_movements(product_id, movements, products):
    product = _find_product(products, product_id)
    if product is None:
        return None

    movements_for_product = [
        movement for movement in movements
        if movement.get("product_id") == product_id
    ]
    return movements_for_product


def get_product_movements_by_type(product_id, movement_type, movements, products):
    product = _find_product(products, product_id)
    if product is None:
        return None

    movements_for_product = [
        movement for movement in movements
        if movement.get("product_id") == product_id
    ]
    return [
        movement for movement in movements_for_product
        if movement.get("type") == movement_type
    ]


def get_product_movements_by_date_range(
    product_id, start_date, end_date, movements, products
):
    product = _find_product(products, product_id)
    if product is None:
        return None

    movements_for_product = [
        movement for movement in movements
        if movement.get("product_id") == product_id
    ]
    return [
        movement
        for movement in movements_for_product
        if start_date <= movement.get("date") <= end_date
    ]


def check_product_movements_integrity(product_id, movements, products):
    product = _find_product(products, product_id)
    if product is None:
        return False

    movements_for_product = [
        movement for movement in movements
        if movement.get("product_id") == product_id
    ]
    return len(movements_for_product) > 0


def _find_product(products, product_id):
    for product in products:
        if product.get("id") == product_id:
            return product
    return None
