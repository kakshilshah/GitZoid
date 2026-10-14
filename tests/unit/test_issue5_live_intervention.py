import pytest


@pytest.mark.parametrize(
    "value,expected",
    [
        ("  Druks  ", "druks"),
        ("STRASSE", "strasse"),
        ("Straße", "strasse"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_strip_casefold_normalization(value, expected):
    assert value.strip().casefold() == expected
