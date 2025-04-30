import pytest
from calculadora.operaciones import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(5, 2) == 3

def test_multiplicar():
    assert multiplicar(4, 5) == 20

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)
