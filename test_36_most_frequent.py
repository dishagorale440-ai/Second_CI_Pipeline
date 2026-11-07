import importlib

module = importlib.import_module("36_most_frequent")


def test_most_frequent_normal_list():
    assert module.most_frequent([1, 2, 2, 3, 2, 4, 4]) == 2


def test_single_element():
    assert module.most_frequent([5]) == 5


def test_all_elements_same():
    assert module.most_frequent([3, 3, 3]) == 3


def test_empty_list():
    assert module.most_frequent([]) is None


def test_negative_numbers():
    assert module.most_frequent([-1, -2, -2, -3]) == -2

