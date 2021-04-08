def stripupper(s):
    return s.strip().upper()


names = ["Php", " Java  ", "c", " python ", "JavaScript", "  C#"]
# for n in sorted(names, key = len):
#     print(n)

for n in sorted(names, key=stripupper):
    print(n.strip())
