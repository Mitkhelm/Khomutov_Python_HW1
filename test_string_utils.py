import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" SkyPro", "SkyPro"),
    (" 123", "123"),
    (" 123 Sky Pro", "123 Sky Pro"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" ", ""),
    ("", ""),
    ("SkyPro", "SkyPro"), 
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, bool", [
    ("SkyPro", "S", True),
    ("123", "1", True),
    ("123 Sky Pro", "2", True),
])
def test_contains_positive(input_str, symbol, bool):
    assert string_utils.contains(input_str, symbol) == bool


@pytest.mark.xfail
@pytest.mark.parametrize("input_str, symbol, bool", [
    ("SkyPro", "h", True),
    ("123", " ", True),
    ("", "2", True),
])
def test_contains_xfail(input_str, symbol, bool):
    assert string_utils.contains(input_str, symbol) == bool


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("123", "1", "23"),
    ("123 Sky Pro", " ", "123SkyPro"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", " ", "SyPro"),
    ("123", "6", "23"),
    ("123 Sky Pro", "S", "123SkyPro"),
])
def test_delete_symbol_xfail(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected