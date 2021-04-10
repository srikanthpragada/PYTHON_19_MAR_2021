# Formal parameter can change actual parameter if it is mutable
def prepend(l, v):
    l.insert(0, v)


lst = [1, 2, 3]
prepend(lst, 10)
print(lst)
