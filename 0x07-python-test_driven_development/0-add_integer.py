#!/usr/bin/python3
"""Module add_integer"""


def add_integer(a, b=98):
    """add_integer.
    Args:
        a: Fisrt number.
        b: second number.
    Returns:
        the add of two numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("test/0.add_integer.txt") 
