import pytest

from doctest_sample import mean


@pytest.mark.parametrize(
    "input_numbers, expected_result",  # nome parametros, pode ser list[str]
    [
        ([1, 2, 3, 4, 5], 3.0),
        ([2.5, 3.75, 1.25, 4], 2.875),
        ([], 0),
    ],  # iteravel
)
def test_mean(input_numbers, expected_result):
    assert mean(input_numbers) == expected_result
