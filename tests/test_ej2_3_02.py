from src.ej2_3_02 import cadena_Numeros, comprobar_Numero
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (5, "1, 3, 5."),
        (1, "1."),
        (2, "1."),
        (20, "1, 3, 5, 7, 9, 11, 13, 15, 17, 19."),
        (10, cadena_Numeros(10))
    ]
)


def test_cadena_Numeros_params(input_n1, expected):
    assert cadena_Numeros(input_n1) == expected


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (10, True),
        (-1, False),
        (5, True),
        (0, False),
        (7, comprobar_Numero(200))
    ]
)


def test_comprobar_Numero_params(input_n1, expected):
    assert comprobar_Numero(input_n1) == expected