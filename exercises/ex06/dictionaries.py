"""Practice with dictionaries."""

__author__ = "730365963"


def invert(a: dict[str, str]) -> dict[str, str]:
    """This dictionary inverts the keys and values of a given dictionary."""
    b: dict[str, str] = {}
    for key in a: 
        if a[key] in b:
            raise KeyError("This key has already been used.")
        b[a[key]] = key
    return b
        

def favorite_color(a: dict[str, str]) -> str:
    """This dictionary will return the color that appears most frequently."""
    b: dict[str, int] = {}
    for key in a:
        color = a[key]
        if color in b:
            b[color] += 1
        else:
            b[color] = 1 
    i: int = 0
    empty: str = ""
    for key in b:
        counter = b[key]
        if counter > i: 
            i = counter
            empty = key  
    return empty


def count(a: list[str]) -> dict[str, int]:
    """Given a list, the dictionary will record the frequency of the given values."""
    b: dict[str, int] = {}
    for item in a: 
        if item in b:
            b[item] += 1
        else:
            b[item] = 1
    return b