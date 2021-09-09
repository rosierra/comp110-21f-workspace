"""Counting letters in a string."""

__author__ = "730365963"

letter_search: str = input("What letter do you want to search for? ")
enter_word: str = input("Enter a word: ")
total: int = 0 
i: int = 0

while i < len(enter_word): 
    if (enter_word[i]) == letter_search:
        total = total + 1
    i = i + 1

print("Count: " + str(total))