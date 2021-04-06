# positional-only arguments
def area(l, w, /):
    return l * w


# print(area(length=10, width=10))
print(area(20, 30))
