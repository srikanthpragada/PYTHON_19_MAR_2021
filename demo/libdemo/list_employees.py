# Print dept name followed by employees using employees.txt

with open("employees.txt", "rt") as f:
    depts = {}
    for line in f.readlines():
        parts = line.split(",")
        if len(parts) < 2:
            continue

        dname = parts[0].strip()
        ename = parts[1].strip()
        if len(dname) == 0 or len(ename) == 0:
            continue

        if dname in depts:
            depts[dname].append(ename)
        else:
            depts[dname] = [ename]

for name, employees in sorted(depts.items()):
    print(name)
    for e in sorted(employees):
        print(f"  {e}")
