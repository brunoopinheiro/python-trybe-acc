import pytest

from price_calculator import calculate_total_price


@pytest.mark.parametrize(
    "unit_price, quantity, discount, expected",
    [
        ("10", 5, 0, TypeError),
        (10, 5.5, 0, TypeError),
        (10, 5, [50], TypeError),
    ],
)
def test_raise_type_error_in_calculate_total_price(
    unit_price, quantity, discount, expected
):
    with pytest.raises(expected):  # TypeError
        calculate_total_price(unit_price, quantity, discount)


@pytest.mark.parametrize(
    "unit_price, quantity, discount, expected",
    [
        (-10, 5, 0, ValueError),
        (0, 5, 0, ValueError),
        (10, -15, 0, ValueError),
        (10, 10, 110, ValueError),
        (10, 10, -110, ValueError),
    ],
)
def test_raise_value_error_in_calculate_total_price(
    unit_price, quantity, discount, expected
):
    with pytest.raises(expected):
        calculate_total_price(unit_price, quantity, discount)


@pytest.mark.parametrize(
    "unit_price, quantity, discount, expected",
    [
        (100, 5, 0, 500),
        (100, 5, 50, 250),
        (100, 5, 90, 50),
    ],
)
def test_correct_behavior_in_calculate_total_price(
    unit_price, quantity, discount, expected
):
    assert calculate_total_price(unit_price, quantity, discount) == expected
