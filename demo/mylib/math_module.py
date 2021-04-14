"""
This module contains functions related to math and numbers
"""

def iseven(n: int) -> bool:
    """
    Takes a number and returns True if it is even number otherwise false
    n : int
    Returns bool
    """
    return n % 2 == 0


def square(n: int) -> int:
    return n * n


# Testing
# __name__ is  __main__  or  math_module
if __name__ == "__main__":
    print("Testing module")
    print(iseven(100))
    print(square(10))
