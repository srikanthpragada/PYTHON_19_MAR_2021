def iseven(n):
    return n % 2 == 0


def square(n):
    return n * n


# Testing
# __name__ is  __main__  or  math_module
if __name__ == "__main__":
    print("Testing module")
    print(iseven(100))
    print(square(10))
