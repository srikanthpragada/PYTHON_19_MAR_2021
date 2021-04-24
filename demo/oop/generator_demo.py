def divisble_By_3_5():
    for n in range(100, 201):
        if n % 3 == 0 and n % 5 == 0:
            yield n


numbers = divisble_By_3_5()
print(type(numbers))
print(next(numbers))
print(next(numbers))