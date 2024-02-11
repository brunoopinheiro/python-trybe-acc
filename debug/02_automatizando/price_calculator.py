def calculate_total_price(unit_price, quantity, discount) -> float:
    if (
        not isinstance(unit_price, (int, float))
        or not isinstance(quantity, int)
        or not isinstance(discount, (int, float))
    ):
        raise TypeError("Invalid input types")

    if unit_price <= 0 or quantity <= 0 or discount < 0 or discount >= 100:
        raise ValueError("Invalid input values")

    total = unit_price * quantity
    total = total - (discount * total / 100)

    return total
