"""Finding duplicate letters in a word."""

__author__ = "730365963"

word: str = input("Enter a word: ")
dup: bool = False 

i: int = 0
j: int = 0

while i < len(word):
    j = i + 1
    while j < len(word):
        if word[j] == word[i]:
            dup = True
        j += 1
    i += 1
   

print(("Found duplicate: " + str(dup)))