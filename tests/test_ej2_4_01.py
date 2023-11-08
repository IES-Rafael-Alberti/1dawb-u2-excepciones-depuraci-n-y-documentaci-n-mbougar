from src.ej2_4_01 import algoritmo_Burbuja
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ([8, 3, 1, 19, 14, 100, 56, 78, 3, 12, 8], [1, 3, 3, 8, 8, 12, 14, 19, 56, 78, 100]),
        ([1, 2], [1, 2]),
        ([19, 3, 5], [3, 5, 19]),
        ([8, 8, 8, 9, 8], [8, 8, 8, 8, 9]),
    ]
)


def test_algoritmo_Burbuja_params(input_n1, expected):
    assert algoritmo_Burbuja(input_n1) == expected