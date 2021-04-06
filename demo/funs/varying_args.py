def wish(*names, message="Hello"):
    for n in names:
        print(f"{message} {n}")


wish("Steve", "Bill")
wish("Mike", "Jack", "Scott", message="Hi")
