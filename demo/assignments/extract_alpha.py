strings = ["  Testing  ", "Map ", " Java 15", "Python 3.9 Version"]


def alphabets(st):
    newst = ""
    for c in st:
        if c.isalpha():
            newst += c

    return newst


for n in map(alphabets, strings):
    print(n)
