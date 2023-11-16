"""Further implementation of unit tests!"""

__author__: str = "730645945"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


# Test cases for the invert function
def test_invert_valid():
    """The function invert should work as a normal function- use case."""
    input_dict: dict[str, str] = {'Alyssa': 'Red', 'Bob': 'Blue', 'Charlie': 'Green'}
    assert invert(input_dict) == {'Red': 'Alyssa', 'Blue': 'Bob', 'Green': 'Charlie'}


def test_invert_empty_value_and_key():
    """The function invert when given dictionary with empty values and keys should return {}- edge case."""
    input_dict: dict[str, str] = {}
    assert invert(input_dict) == {}


def test_invert_duplicate_values():
    """The function invert should raise a KeyError for dictionaries with duplicate values- use case."""
    with pytest.raises(KeyError):
        my_dictionary = {'Alyssa': 'Red', 'Bob': 'Blue', 'Charlie': 'Green', 'Dave': 'Green'}
        invert(my_dictionary)


# Test cases for the favorite_color function
def test_favorite_color_valid():
    """The function favorite_color should work as a normal function- use case."""
    color_dict: dict[str, str] = {'Alice': 'Red', 'Bob': 'Blue', 'Charlie': 'Red', 'David': 'Green'}
    assert favorite_color(color_dict) == "Red"


def test_favorite_color_empty_value_and_key():
    """The function favorite_color when given dictionary with empty values and keys should return " "- edge case."""
    color_dict: dict[str, str] = {}
    assert favorite_color(color_dict) == " "


# Test cases for the favorite_color function
def test_favorite_color_tie():
    """The function favorite_color should handle a tie between multiple colors- edge case."""
    color_dict: dict[str, str] = {'Alice': 'Red', 'Bob': 'Blue', 'Charlie': 'Red', 'David': 'Blue'}
    assert favorite_color(color_dict) in {'Red', 'Blue'}


# Test cases for the count function
def test_count_valid():
    """The function count should work as a normal function- use case."""
    input_list: list[str] = ['apple', 'banana', 'apple', 'cherry', 'banana']
    assert count(input_list) == {'apple': 2, 'banana': 2, 'cherry': 1}


def test_count_empty():
    """The function count when given empty list should return " "- edge case."""
    input_list: list[str] = []
    assert count(input_list) == {}


# Test cases for the count function
def test_count_duplicate_values():
    """The function count should handle lists with duplicate values- use case."""
    input_list: list[str] = ['apple', 'banana', 'apple', 'cherry', 'banana', 'cherry']
    assert count(input_list) == {'apple': 2, 'banana': 2, 'cherry': 2}


# Test cases for the alphabetizer function
def test_alphabetizer_valid():
    """The function alphabetizer should work as a normal function- use case."""
    word_list: list[str] = ['apple', 'banana', 'cherry', 'apricot']
    assert alphabetizer(word_list) == {'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry']}


def test_alphabetizer_empty():
    """The function alphabetizer when given empty list should return []- edge case."""
    input_list: list[str] = []
    assert alphabetizer(input_list) == {}


# Test cases for the alphabetizer function
def test_alphabetizer_case_insensitive():
    """The function alphabetizer should be case-insensitive- use case."""
    word_list: list[str] = ['Apple', 'banana', 'Cherry', 'apricot']
    assert alphabetizer(word_list) == {'a': ['Apple', 'apricot'], 'b': ['banana'], 'c': ['Cherry']}


# Test cases for the update_attendance function
def test_update_attendance_valid():
    """The function update_attendance should work as a normal function- use case."""
    attendance_dict: dict[str, list[str]] = {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Charlie']}
    day: str = 'Monday'
    student: str = 'David'
    assert update_attendance(attendance_dict, day, student) == {'Monday': ['Alice', 'Bob', 'David'], 'Tuesday': ['Charlie']}


def test_update_attendance_new_day():
    """The function update_attendance should add a new day and student correctly- use case."""
    attendance_dict: dict[str, list[str]] = {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Charlie']}
    day: str = 'Wednesday'
    student: str = 'Eve'
    assert update_attendance(attendance_dict, day, student) == {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Charlie'], 'Wednesday': ['Eve']}


# Test case for the update_attendance function
def test_update_attendance_empty_dict():
    """The function update_attendance should handle an empty attendance dictionary- edge case."""
    attendance_dict: dict[str, list[str]] = {}
    day: str = 'Monday'
    student: str = 'Alice'
    assert update_attendance(attendance_dict, day, student) == {'Monday': ['Alice']}

    