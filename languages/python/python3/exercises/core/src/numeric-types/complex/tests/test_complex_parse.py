from ..complex_parse import parse_complex_str


def test_expected_behaviour():
    assert parse_complex_str("3+4j") == 3 + 4j
    assert parse_complex_str("-2.5-1.5j") == -2.5 - 1.5j
    assert parse_complex_str("-4j") == -4j
    assert parse_complex_str("10.5") == 10.5 + 0j
