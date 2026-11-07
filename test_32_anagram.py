# Test cases for Program 32

import importlib

module = importlib.import_module("32_anagram")


def test_anagram_true():
    assert module.is_anagram("listen", "silent") is True


def test_anagram_false():
    assert module.is_anagram("hello", "world") is False


def test_anagram_uppercase():
    assert module.is_anagram("Listen", "Silent") is True


def test_anagram_with_spaces():
    assert module.is_anagram("school master", "the classroom") is True


def test_anagram_empty():
    assert module.is_anagram("", "") is True