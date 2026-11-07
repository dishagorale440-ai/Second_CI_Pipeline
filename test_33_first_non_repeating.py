import importlib

module = importlib.import_module("33_first_non_repeating")


def test_normal():
    assert module.first_non_repeating_char("Swiss") == "w"


def test_first_character():
    assert module.first_non_repeating_char("apple") == "a"


def test_no_repeating():
    assert module.first_non_repeating_char("aabb") is None


def test_empty():
    assert module.first_non_repeating_char("") is None