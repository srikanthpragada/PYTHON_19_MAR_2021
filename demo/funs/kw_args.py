def fun(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def fun2(*args, **kwargs):
    pass


fun(a=10, b=20, c="abc")
fun2(10, 20, 30, name="Abc", age=20)
