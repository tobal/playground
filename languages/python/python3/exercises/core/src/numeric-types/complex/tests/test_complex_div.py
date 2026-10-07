from ..complex_div import safe_complex_div
from pytest import raises


def test_naive_division():
    assert safe_complex_div(1 + 2j, 3 + 4j) == (0.44 + 0.08j)


def test_scaled_division():
    assert safe_complex_div(1 + 1j, 1e200 + 1e200j) == (1e-200 + 0j)


def test_raises_zero_div_error():
    with raises(ZeroDivisionError):
        safe_complex_div(1 + 2j, 0 + 0j)
