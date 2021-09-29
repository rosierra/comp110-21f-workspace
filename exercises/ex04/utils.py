"""List utility functions."""

__author__ = "730365963"


def all(integers: list[int], numbers: int) -> bool:
    """Return True if all numbers match indicated number, False if not."""
    i: int = 0 
    while i < len(integers):
        if integers[i] == numbers:
            return True
            i += 1
        else:
            return False
    return True


def is_equal(first: list[int], second: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    i: int = 0
    while i < len(first):
        if first[i] == second[i]:
            return True
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Return the largest value in a list."""
    i: int = 0 
    max_value: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(input):
        if max_value < input[i]:
            max_value = input[i]
            i += 1
        else:
            i += 1 
    return max_value