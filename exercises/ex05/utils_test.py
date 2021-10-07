"""Unit tests for list utility functions."""


__author__ = "730365963"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_four_items() -> None:
    """Test the ability to return even numbers in a list of four items."""
    nums: list[int] = [1, 2, 3, 4]
    assert only_evens(nums) == [2, 4]


def test_only_evens_all_odd() -> None:
    """Test the result of a single item in an list."""
    nums: list[int] = [1, 3, 5, 7]
    assert only_evens(nums) == []


def test_only_evens_empty() -> None:
    """Test the result of an empty list."""
    nums: list[int] = []
    assert only_evens(nums) == []


def test_sub_multiple() -> None: 
    """Test the result of multiple integers for the subset list."""
    a_list: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    x: int = 2
    y: int = 8
    assert sub(a_list, x, y) == [30, 40, 50, 60, 70, 80]


def test_sub_random() -> None: 
    """Test random integers in the subset list."""
    a_list: list[int] = [3, 6, 4, 8, 27]
    x: int = 1
    y: int = 3
    assert sub(a_list, x, y) == [6, 4]


def test_sub_end_index() -> None: 
    """Test an end index greater than length of the list."""
    a_list: list[int] = [45, 67, 89, 20, 34]
    x: int = 2
    y: int = 6
    assert sub(a_list, x, y) == [89, 20, 34]


def test_concat_combine_equal() -> None:
    """Test if lists of equal lengths concatenate."""
    first: list[int] = [1, 2, 3]
    second: list[int] = [4, 5, 6]
    assert concat(first, second) == [1, 2, 3, 4, 5, 6]


def test_concat_combine_different() -> None:
    """Test concatenation of different length lists."""
    first: list[int] = [2, 4, 6, 8]
    second: list[int] = [10, 12]
    assert concat(first, second) == [2, 4, 6, 8, 10, 12]


def test_concat_empty() -> None: 
    """Test the concatenation of empty lists."""
    first: list[int] = []
    second: list[int] = []
    assert concat(first, second) == []
