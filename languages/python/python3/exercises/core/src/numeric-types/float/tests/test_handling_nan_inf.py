from ..handling_nan_inf import clean_float_array


def test_normal_values_unchanged():
    input_list = [1.0, 2.0, -3.0]
    expected = [1.0, 2.0, -3.0]
    assert clean_float_array(input_list) == expected


def test_nan_values_changed_to_fallback():
    input_list = [1.0, 2.0, float('nan')]
    expected = [1.0, 2.0, 1.2]
    assert clean_float_array(input_list, fallback=1.2) == expected


def test_inf_values_changed_to_fallback():
    input_list = [1.0, 2.0, float('inf'), -float('inf')]
    expected = [1.0, 2.0, 1.2, 1.2]
    assert clean_float_array(input_list, fallback=1.2) == expected


def test_expected_behaviour():
    input_list = [1.0, float('nan'), float('inf'), -float('inf'), 3.5]
    expected = [1.0, -1.0, -1.0, -1.0, 3.5]
    assert clean_float_array(input_list, fallback=-1.0) == expected
