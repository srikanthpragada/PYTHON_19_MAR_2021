def next_even(n):
    if n % 2 == 0:
        return n + 2
    else:
        return n + 1


def next_odd(n):
    return n + 2 if n % 2 == 1 else n + 1


v = next_even(11)
# v = next_even('abc')
print(v)
