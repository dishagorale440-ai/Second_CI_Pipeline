import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_string_by_two():
    assert module.rotate_string("Python", 2) == "onPyth"


def test_rotate_string_by_zero():
    assert module.rotate_string("Python", 0) == "Python"


def test_rotate_string_by_full_length():
    assert module.rotate_string("Python", 6) == "Python"


def test_rotate_string_empty():
    assert module.rotate_string("", 3) == ""


def test_rotate_string_more_than_length():
    assert module.rotate_string("abcd", 6) == "cdab"

