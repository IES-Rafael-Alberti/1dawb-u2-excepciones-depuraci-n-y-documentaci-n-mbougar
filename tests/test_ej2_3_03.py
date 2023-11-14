from src.ej2_3_03 import cadena_Numeros
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (5, "5, 4, 3, 2, 1, 0."),
        (1, "1, 0."),
        (2, "2, 1, 0."),
        (20, "20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0."),
        (10, cadena_Numeros(10))
    ]
)


def test_cadena_Numeros_params(input_n1, expected):
    assert cadena_Numeros(input_n1) == expected

