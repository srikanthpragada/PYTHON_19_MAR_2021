g = 100  # Global variable


def f1():
    global g
    g = g + 10
    a = 10  # Enclosing variable
    print("f1()")

    def f2():
        nonlocal a
        b = 200  # Local Variable
        a = a + 1
        print(b, a, g)

    f2()
    print('a = ', a)


f1()
