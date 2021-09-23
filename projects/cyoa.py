"""The Python Olympics."""

__author__ = "730365963"

from random import randint

chances: int = 3
player: str 
points: int = 0

GYMNAST_EMOJI: str = '\U0001f938'
WRESTLER_EMOJI: str = '\U0001f93C'
SWIMMER_EMOJI: str = '\U0001f3CA'
SMILEYFACE_EMOJI: str = '\U0001f604'
SADFACE_EMOJI: str = '\U0001f62D'
WOOO_EMOJI: str = '\U0001f64C'
BRONZE_EMOJI: str = '\U0001f949'
SILVER_EMOJI: str = '\U0001f948'
GOLD_EMOJI: str = '\U0001f947'


def main() -> None:
    """Entrypoint of the program."""
    global player
    global points
    greet()
    begin()
    

def greet() -> None:
    """Beginning of the experience."""
    global player
    player = input(str("Enter your name: "))
    print("\n")
    print(f"Welcome to the 2021 Python Olympics, {player}!")
    print("\n")
    print("This year, we have decided to open up the games to everyone.")
    print("You may participate in up to three categories.")
    print("Which medal you earn will depend on how many games you can win.")
    print("\n")
    print("You have three chances to earn a max of three points.")
    print(f"3 points will earn you a Gold Medal {GOLD_EMOJI}, 2 points will earn you a Silver Medal {SILVER_EMOJI}, and 1 point will earn you a Bronze Medal {BRONZE_EMOJI}.")
    print("\n")
    print("Type 'end' to end the game when you are out of chances.")
    print("\n")
    starting_point: str = str(input("Type 'yes' if you are ready to begin: "))
    if starting_point == "yes":
        print("\n")
        begin()
        

def count() -> None:
    """Chance count"""
    global chances
    chances -= 1
    print(f"You have {chances} chances left to participate in a category.")
    if chances <= 0:
        print("Unfortunately, you have used up all of your chances!")
        print("\n")
        end()
        

def begin() -> None:
    """The game arena where you can choose your category."""
    print("Welcome to the game arena! Which category would you like to participate in now? ")
    category: str = str(input("gymnastics, wrestling, swimming, or end: "))
    print("\n")
    if category == "gymnastics":
        gymnastics()
    else:
        if category == "wrestling":
            wrestling(points)
        else: 
            if category == "swimming":
                swimming()
            else: 
                if category == "end":
                    end()


def gymnastics() -> None:
    """Gymnastics category game."""
    global player
    global points
    print(f"Welcome to the gymnastics category, {player}! {GYMNAST_EMOJI}")
    print("\n")
    print("In this round, you will decide what to include in your routine.")
    routine_choice: str = str(input("Type 'handstand' or 'cartwheel': "))
    print("\n")
    if routine_choice == "handstand":
        print(f"Oh no! You accidentally fell over and lost your point {SADFACE_EMOJI}.")
        print(f"You have {points} point(s).")
        print("\n")
    else: 
        if routine_choice == "cartwheel":
            print(f"That was executed beautifully! You earned one point! {WOOO_EMOJI}")
            points = points + 1
            print(f"You now have {points} point(s).")
            print("\n")
        else:
            print("I'm not sure what you were trying to do there. Please try again!")
            print("\n")
            gymnastics()
    count()
    print("\n")
    begin()


def wrestling(x: int) -> int: 
    """Wresting category game."""
    global points
    print(f"Welcome to the wrestling category! {WRESTLER_EMOJI}")
    print("\n")
    print("Python will use your age to make sure you're old enough to participate in this category.")
    user_age: int = int(input("Input your age here: "))
    print("\n")
    if user_age >= 17:
        print("Congratulations! You competed in the wrestling category and won against your component.")
        points = points + 1
        print(f"You earned one point, which means you have {points} point(s).")
        print("\n")
    else: 
        if user_age < 17:
            print(f"Sadly, you are too young to participate. Try another category! You still have {points} points.")
            print("\n")
    count()
    print("\n")
    begin()
    return points
    

def swimming() -> None:
    """Swimming category game."""
    global points
    print(f"Welcome to the swimming category! I hope you're ready to get your splash on. {SWIMMER_EMOJI}")
    print("\n")
    print("In this category, you are going to guess how many laps you will be able to swim: 29 or 30.")
    laps: int = int(input("How many laps will you be able to swim? "))
    print("\n")
    if laps == randint(29, 30):
        print("You guessed just right! You swam fantastically, and earned one point.")
        points = points + 1
        print(f"You now have {points} points. Great job!")
        print("\n")
        count()
        begin()
    else: 
        print("Oh no! You didn't quite hit the mark.")
        print(f"You still have {points} point(s).")
        print("\n")
    count()
    begin()
    

def end() -> None:
    print("Congratulations! You have completed the Python Olympics.")
    print("\n")
    print("Let's count up your points and see what you won.")
    if points == 0:
        print("Sadly, you did not win any games, so you are not eligible for a medal. Hope to see you next time!")
    else:
        if points == 1:
            print(f"Wowee! You have one point, which means you won a Bronze Medal {BRONZE_EMOJI}. Congrats!")
            print("\n")
        else:
            if points == 2:
                print(f"Second is the best! You have 2 points, which means you are a Silver Medalist {SILVER_EMOJI}. Amazing work!")
                print("\n")
            else:
                if points == 3:
                    print(f"You're giving Michael Phelps a run for his money. You have 3 points, which means you won the Gold Medal {GOLD_EMOJI}. Congratulations!")
                    print("\n")
    options: str = str(input("Type 'restart' to restart the game, and 'stop' to stop playing: "))
    if options == "restart":
        main()
    else: 
        if options == "stop":
            print(f"Thanks for playing! We can't wait see you for the 2025 Python Olympics {SMILEYFACE_EMOJI}")


if __name__ == "__main__":
    main()
