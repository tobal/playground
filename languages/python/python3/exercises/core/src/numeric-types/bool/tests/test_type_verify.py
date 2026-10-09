from ..type_verify import count_pure_booleans


def test_can_count_booleans_in_list():
    assert count_pure_booleans([True, 1, 0, False, "True", True]) == (2, 1)
