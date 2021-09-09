"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730365963"

from random import randint

print("Your fortune cookies says...")
fortune_cookie: int = int(randint(1, 4))

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