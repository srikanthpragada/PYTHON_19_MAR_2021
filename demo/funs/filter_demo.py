strings = ['abc', '34343', '12', 'xyz', 'abc123']


def hasdigit(st):
    for c in st:
        if c.isdigit():
            return True

    return False


for n in filter(str.isdigit, strings):
    print(n)

for n in filter(hasdigit, strings):
    print(n)
