"""Repeating a beat in a loop."""

__author__ = "730365963"


beat: str = input("What beat do you want to repeat? ")  # Begin your solution here...

repeated_beat: int = int(input("How many times do you want to repeat it? "))

i = 0
beat_count = ""

if repeated_beat <= 0: 
    print("No beat...")
else: 
    while i < repeated_beat:
        if i < repeated_beat - 1:
            beat_count = beat_count + beat + " "
        else: 
            beat_count = beat_count + beat
        i = i + 1
    print(beat_count)