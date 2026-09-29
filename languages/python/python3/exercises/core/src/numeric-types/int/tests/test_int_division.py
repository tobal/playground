from ..int_division import divide_integer_modes
import pytest


def test_true_division_returns_float():
    true_div_value = divide_integer_modes(10, 5)[1]
    assert true_div_value == 2.0


def test_floor_division_returns_int():
    floor_div_value = divide_integer_modes(10, 5)[0]
    assert floor_div_value == 2


def test_modulo_returns_int():
    floor_div_value = divide_integer_modes(10, 5)[2]
    assert floor_div_value == 0


def test_raises_error_if_cannot_divides_by_0():
    with pytest.raises(ZeroDivisionError):
        divide_integer_modes(10, 0)
    

def test_exercise_pass():
    assert divide_integer_modes(10, 3) == (3, 3.3333333333333335, 1)
    assert divide_integer_modes(10, 2) == (5, 5.0, 0)
