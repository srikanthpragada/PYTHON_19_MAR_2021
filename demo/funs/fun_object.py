def fun():
    print("First fun")


oldfun = fun


def fun(msg):
    print("Fun with message :", msg)


oldfun()
fun("Hello")
