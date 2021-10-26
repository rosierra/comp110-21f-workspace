"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest


__author__ = "730365963"


def test_invert_multiple() -> None:
    """Test the ability to invert the keys and values of a given dictionary."""
    a: dict[str, str] = {"state": "Virginia", "beach": "Virginia beach"}
    assert invert(a) == {"Virginia": "state", "Virginia beach": "beach"}


def test_invert_same_key() -> None:
    """Test the ability to raise a key error when the same key is used more than once."""
    a: dict[str, str] = {"apple": "banana", "strawberry": "orange"}
    assert invert(a) == {"banana": "apple", "orange": "strawberry"}


def test_invert_again() -> None:
    """Test the ability to invert the keys and values of a given dictionary."""
    a: dict[str, str] = {"love": "you"}
    assert invert(a) == {"you": "love"}


def test_favorite_color_many() -> None:
    """Test the ability to return the most frequently used color."""
    a: dict[str, str] = {"Sierra": "yellow", "Amina": "purple", "Becca": "purple"}
    assert favorite_color(a) == "purple"


def test_favorite_color_even() -> None:
    """Test the ability to return first value if all are even."""
    a: dict[str, str] = {"Sierra": "yellow", "Amina": "purple", "Amaya": "blue"}
    assert favorite_color(a) == "yellow"


def test_favorite_color_single() -> None:
    """Test the ability to return first value if only one color."""
    a: dict[str, str] = {"Sierra": "yellow"}
    assert favorite_color(a) == "yellow"


def test_count_frequency_of_pets() -> None:
    """Test the ability to count frequency of pets."""
    a: list[str] = ["dog", "cat", "cat", "dog", "snake"]
    assert count(a) == {"dog": 2, "cat": 2, "snake": 1}


def test_count_frequency_of_marbles() -> None:
    """Test the ability to count frequency of marbles."""
    a: list[str] = ["red", "white", "red", "white", "red", "red"]
    assert count(a) == {"red": 4, "white": 2}


def test_count_frequency_of_friends() -> None:
    """Test the ability to count frequency of friends' names."""
    a: list[str] = ["Adrian", "Alvin", "Maria", "Maria", "Felicia"]
    assert count(a) == {"Adrian": 1, "Alvin": 1, "Maria": 2, "Felicia": 1}


def test_invert_key_error() -> None:
    """Test raise key error."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)