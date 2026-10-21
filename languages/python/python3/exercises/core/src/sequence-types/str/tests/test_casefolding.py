from ..casefolding import normalize_and_casefold


def test_casefold():
    assert normalize_and_casefold("Straße") == "strasse"


def test_normalize():
    assert normalize_and_casefold("e\u0301") == normalize_and_casefold("\u00e9")

