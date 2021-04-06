# keyword only params
def area(*, width, length):
    return length * width


print(area(length=10, width=10))
print(area(width=20, length=10))
