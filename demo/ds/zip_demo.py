names = ['Java', 'Python', 'C#', 'Typescript']
versions = [16, 3.9, 10]

# for i, n in enumerate(names):
#     print(n, versions[i])

for n, v in zip(names, versions):
    print(n, v)
