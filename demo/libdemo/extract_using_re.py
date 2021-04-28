import re

st = input("Enter string :")
m = re.search('[a-zA-Z]', st)
if m is None:
    print("Sorry! Not found!")
else:
    print(st[m.start():])
