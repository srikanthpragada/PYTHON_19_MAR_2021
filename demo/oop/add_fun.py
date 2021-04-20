def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return int(a) + int(b)


print(add(10, 20))
print(add("10", "20"))
