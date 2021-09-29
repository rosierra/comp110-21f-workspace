"""Drawing forests in a loop."""

__author__ = "730365963"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
tree_str: str = ""

i: int = 0
j: int = 0 

while i < depth: 
    if j < depth: 
        print(TREE)
    if depth == 4:
        print(TREE + TREE + TREE + TREE)
        j += 1
    i += 1