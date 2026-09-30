from ..modular_exponentiation import custom_pow_mod
import pytest

def test_small_exponent():
    assert custom_pow_mod(2, 10, 1000) == 24


def test_large_exponent():
    assert custom_pow_mod(7, 256, 13) == 9


def test_huge_exponent():
    assert custom_pow_mod(7, 100000, 5) == 1


def test_raises_value_error_for_negative_exponent():
    with pytest.raises(ValueError):
        custom_pow_mod(1, -1, 1)


def test_raises_value_error_for_not_positive_mod():
    with pytest.raises(ValueError):
        custom_pow_mod(1, 1, 0)
    with pytest.raises(ValueError):
        custom_pow_mod(1, 1, -1)
