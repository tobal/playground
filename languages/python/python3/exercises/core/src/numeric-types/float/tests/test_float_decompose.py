from ..float_decompose import decompose_float


def test_zero_denominator():
    assert decompose_float(1.0) == (1, 1, False)


def test_fraction():
    assert decompose_float(0.75) == (3, 4, False)


def test_can_handle_zero():
    assert decompose_float(0.0) == (0, 1, False)


def test_detects_negative_zero():
    assert decompose_float(-0.0) == (0, 1, True)
