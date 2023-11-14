from src.ej2_3_01 import calcular_Años, comprobar_Numero
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (5, "1-2-3-4-5."),
        (1, "1."),
        (2, "1-2."),
        (20, "1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20."),
        (10, calcular_Años(10))
    ]
)


def test_calcular_Años_params(input_n1, expected):
    assert calcular_Años(input_n1) == expected


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (5, True),
        (1, True),
        (-2, False),
        (0, False),
        (10, comprobar_Numero(10))
    ]
)


def test_comprobar_Numero_params(input_n1, expected):
    assert comprobar_Numero(input_n1) == expected
