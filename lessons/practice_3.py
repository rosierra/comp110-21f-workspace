"""Nested Loop Practice."""

i: int = 0
j: int = 0
total: int = 0

while i < 10: 
    i += 1
    j = 0
    while j < 5:
        total += 1
        j += 1

print(total)
