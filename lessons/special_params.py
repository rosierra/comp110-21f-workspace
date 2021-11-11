"""Messing around with special parameters."""


from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting function."""
    result: str = "Hello, "
    if isinstance(name, str):
        return result + name
    elif isinstance(name, float):
        return result + "alien from sector " + str(name)
    else:
        return result + "COMP" + str(name)


# Calling hello with no arguments leads to use of default value.
print(hello())
# Calling hello with no argument overrides the default value. 
print(hello("John"))
print(hello(110))
print(hello(3.14))


def add(rhs: Union[str, float] = 0.0, lhs: float = 0.0, ) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result


print(add())   
print(add(110.0))
print(add("Hello"))
