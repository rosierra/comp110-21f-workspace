"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730365963"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

fortune_cookie: int = int(randint(1, 4))
print("Your fortune cookie says...")

if fortune_cookie == 1:
    print("You will get an A in all your classes, even if you didn't drink from the Old Well on the first day of class.")
else:
    if fortune_cookie == 2:
        print("A friendly stranger will compliment your vibes tomorrow.")
    else:
        if fortune_cookie == 3:
            print("You will find joy in the little moments to come.")
        else:
            if fortune_cookie == 4: 
                print("Life will soon be filled with excitement and adventure.")

print("Now, go spread positive vibes!")