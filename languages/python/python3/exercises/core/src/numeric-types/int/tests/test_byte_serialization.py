from ..byte_serialization import int_to_signed_bytes, signed_bytes_to_int


def test_zero_to_bytes():
    assert int_to_signed_bytes(0) == b'\x00'


def test_negative_to_bytes():
    assert int_to_signed_bytes(-128) == b'\xff\x80'


def test_multiple_bytes():
    assert int_to_signed_bytes(1000) == b'\x03\xe8'


def test_edge_cases():
    assert int_to_signed_bytes(127) == b'\x7f'
    assert int_to_signed_bytes(128) == b'\x00\x80'
    assert int_to_signed_bytes(-1) == b'\xff'


def test_roundtrip():
    n = 1256
    assert signed_bytes_to_int(int_to_signed_bytes(n)) == n
