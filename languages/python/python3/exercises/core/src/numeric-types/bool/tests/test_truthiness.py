from ..truthiness import resolve_first_truthy


def test_returns_first_truthy():
    assert resolve_first_truthy("", [], 0, "hello", "world") == "hello"


def test_can_return_default_value():
    assert resolve_first_truthy(None, False, 0.0, default="fallback") == "fallback"
