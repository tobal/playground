from ..runlength import run_length_encode
import pytest


def test_empty_string():
    assert run_length_encode("") == ""


def test_one_character():
    assert run_length_encode("a") == "a1"


def test_longer_string():
    assert run_length_encode("AAABBC") == "A3B2C1"


def test_longest_string():
    assert run_length_encode("AAABBCRRRRRRRRRDDDEEEEEEEEEPPNNNNNNNNNVVV") == "A3B2C1R9D3E9P2N9V3"


def test_numeric_causes_error():
    with pytest.raises(ValueError):
        run_length_encode("A2B")


def test_non_consecutive_runs():
    assert run_length_encode("ABA") == "A1B1A1"
    assert run_length_encode("AABBAA") == "A2B2A2"

