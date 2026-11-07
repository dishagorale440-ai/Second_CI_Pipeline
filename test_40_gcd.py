import importlib

module = importlib.import_module("40_gcd")


def test_gcd_normal_numbers():
    assert module.find_gcd(12, 18) == 6


def test_gcd_equal_numbers():
    assert module.find_gcd(7, 7) == 7


def test_gcd_with_one():
    assert module.find_gcd(15, 1) == 1


def test_gcd_with_zero():
    assert module.find_gcd(10, 0) == 10


def test_gcd_negative_numbers():
    assert module.find_gcd(-12, 18) == 6

