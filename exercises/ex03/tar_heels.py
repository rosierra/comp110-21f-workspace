"""An exercise in remainders and boolean logic."""

__author__ = "730365963"

tar_heels: int = int(input("Enter an int: "))  # Begin your solution here...

if tar_heels % 2 == 0 and tar_heels % 7 == 0:
    print("TAR HEELS")
else:
    if tar_heels % 2 == 0:
        print("TAR")
    else:
        if tar_heels % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA") 