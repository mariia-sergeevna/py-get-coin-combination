import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_combination",
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="should return 1 penny"
                     ),
        pytest.param(6, [1, 1, 0, 0],
                     id="should return 1 penny and 1 nickel"
                     ),
        pytest.param(17, [2, 1, 1, 0],
                     id="should return [2, 1, 1, 0]"
                     ),
        pytest.param(50, [0, 0, 0, 2],
                     id="should return 2 quarters"
                     ),
    ]
)
def test_coin_combination(cents: int, expected_combination: list) -> None:
    assert get_coin_combination(cents) == expected_combination
