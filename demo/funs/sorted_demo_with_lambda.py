names = ["Php", " Java  ", "c", " python ", "JavaScript", "  C#"]
# for n in sorted(names, key = len):
#     print(n)

for n in sorted(names, key=lambda v: v.strip().upper()):
    print(n.strip())
