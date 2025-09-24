import pytest
from app import soma, subtracao, multiplicacao, divisao, eh_par

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(10, 5) == 5

def test_multiplicacao():
    assert multiplicacao(4, 3) == 12

def test_divisao():
    assert divisao(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)

def test_eh_par_true():
    assert eh_par(4) is True

def test_eh_par_false():
    assert eh_par(5) is False
