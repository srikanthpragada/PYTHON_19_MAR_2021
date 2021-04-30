import re

f = open("customers.txt", "rt")
customers = {}
for line in f:
    # Look for name
    m = re.search('[A-Za-z ]+', line)
    if m is None:
        continue

    name = m.group().strip()
    if len(name) == 0:
        continue

    # Look for number
    m = re.search(r'\d+', line)
    if m is None:
        continue

    customers[name] = m.group()

f.close()

for name, number in sorted(customers.items()):
    print(f"{name:15} {number}")
