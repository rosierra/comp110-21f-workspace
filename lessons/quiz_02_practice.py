def odd_and_even(ab: list[int]) -> list[int]:
    i: int = 0
    nums: list[int] = []
    while i < len(ab):
        if i % 2 == 0 and ab[i] % 2 != 0:
            nums.append(ab[i])
        i += 1
    return nums


ab = [2, 9, 4, 17, 9, 10, 15, 13, 14, 21]
print(odd_and_even(ab))


def vowels_and_threes(ab: list[str]) -> str:
    """Return a substring of characters."""
    i: int = 0
    j: int = 0
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    new_string: str = ""
    is_vowel: bool = False
    while i < len(ab):
        is_vowel = False
        j = 0
        while j < len(vowels):
            if vowels[j] == ab[i]:
                is_vowel = True
            j += 1
        if i % 3 == 0 or is_vowel:
            new_string += ""
        elif i % 3 == 0: 
            new_string += ab[i]
        elif is_vowel:
            new_string += ab[i]
        i += 1
    return new_string
