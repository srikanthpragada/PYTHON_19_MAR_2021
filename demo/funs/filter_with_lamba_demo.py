strings = ['abc', '34343', '12', 'xyz', 'abc123']
nums = [10, -10, 22, -30, 40]


def hasdigit(st):
    for c in st:
        if c.isdigit():
            return True

    return False


for n in filter(str.isdigit, strings):
    print(n)

for n in filter(hasdigit, strings):
    print(n)

for n in filter(lambda v: v >= 0, nums):
    print(n)

for n in filter(lambda v: v < 0, nums):
    print(n)

def ispositive(v):
    return v >= 0
