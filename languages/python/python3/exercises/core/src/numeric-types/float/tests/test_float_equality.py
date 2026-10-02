from ..float_equality import is_float_close


def test_simple_example():
    assert is_float_close(0.1 + 0.2, 0.3)


def test_small_numbers():
    assert is_float_close(1e-9, 2e-9, abs_tol=1e-8)


def test_falsy_equation():
    assert not is_float_close(1.0, 1.001, rel_tol=1e-4)
