"""Drawing forests in a loop."""

__author__ = "730365963"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
line = 0
emoji = 1

while depth != line: 
    print(TREE * emoji)
    line += 1
    emoji += 1