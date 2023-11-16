"""Test my zip function."""

__author__ = "730645945"

from lessons.zip import zip

# test_zip_function_test.py


def test_empty_lists() -> None:
    """Tests to see if lists are empty."""
    list1 = []
    list2 = []
    result = zip(list1, list2)
    assert result == {}, "Empty lists should result in an empty dictionary."


def test_lists_of_equal_length() -> None:
    """Tests to see if lists are equal length."""
    list1 = ["apple", "banana", "cherry"]
    list2 = [1, 2, 3]
    result = zip(list1, list2)
    expected = {"apple": 1, "banana": 2, "cherry": 3}
    assert result == expected, "Zip should create a dictionary from two lists of equal length."


def test_unequal_length_lists() -> None:
    """Tests to see if lists are different lengths."""
    list1 = ["apple", "banana", "cherry"]
    list2 = [1, 2]
    result = zip(list1, list2)
    assert result == {}, "Zip should return an empty dictionary when given lists of unequal length."
