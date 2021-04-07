def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def operation(a, b, func):
    return func(a, b)


print(operation(10, 20, add))
print(operation(10, 20, multiply))
