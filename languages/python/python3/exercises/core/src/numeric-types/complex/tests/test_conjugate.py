from ..conjugate import analyze_complex


def test_can_get_real_part():
    (real, _, _) = analyze_complex(2 + 3j)
    assert real == 2.0


def test_can_get_imaginary_part():
    (_, imag, _) = analyze_complex(2 + 3j)
    assert imag == 3.0


def test_can_get_conjugate():
    (_, _, conj) = analyze_complex(2 + 3j)
    assert conj == 2 - 3j


def test_expected_behaviour():
    assert analyze_complex(3 + 4j) == (3.0, 4.0, (3-4j))
    assert analyze_complex(5.0) == (5.0, 0.0, (5+0j))
