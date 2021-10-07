"""List utility functions part 2."""

__author__ = "730365963"


def only_evens(nums: list[int]) -> list[int]:
    """Returns a list containing only the elements of the list that are even."""
    i: int = 0 
    even_list: list[int] = []
    while i < len(nums):
        if nums[i] % 2 == 0:
            even_list.append(nums[i])
        i += 1

    return even_list


print(only_evens([4, 4, 4]))


def sub(a_list: list[int], x: int, y: int) -> list[int]:
    """Generates a list which is a subset of the given list."""
    ab: list[int] = []
    empty_list: list[int] = []
    if x < 0: 
        x = 0
    if y > len(a_list):
        y = len(a_list) 
    if len(a_list) == 0:
        return empty_list 
    if x > len(a_list):
        return empty_list
    if y <= 0: 
        return empty_list
    i: int = x
    while i < y:
        x = a_list[i]
        ab.append(x)
        i += 1
    return ab


a_list = [10, 20, 30, 40]
print(sub(a_list, 1, 3))
    

def concat(first: list[int], second: list[int]) -> list[int]:
    """Generates a list which contains all the elements of the first list followed by all the elements of the second list."""
    combined_list: list[int] = []
    combined_list = first + second 
    return combined_list


print(concat([1, 2, 3], [4, 5, 6]))