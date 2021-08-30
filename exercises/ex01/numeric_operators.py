"""Practice with numeric operators, type conversions, and string concatenation."""

__author__ = "730365963"

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))

left_hand: str = str(left_hand_side)
right_hand: str = str(right_hand_side)

print(left_hand + (" ** ") + right_hand + (" is ") + str(left_hand_side ** right_hand_side))
print(left_hand + (" / ") + right_hand + (" is ") + str(left_hand_side / right_hand_side))
print(left_hand + (" // ") + right_hand + (" is ") + str(left_hand_side // right_hand_side))
print(left_hand + (" % ") + right_hand + (" is ") + str(left_hand_side % right_hand_side))