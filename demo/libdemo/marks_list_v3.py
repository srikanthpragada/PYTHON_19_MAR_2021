# Print name and avg marks from marks.txt

f = open("marks.txt", "rt")
students = {}
for line in f.readlines():
    parts = line.split(",")
    if len(parts) < 2:
        continue  # Ignore line and move to next line

    name = parts[0]
    marks = []
    count = 0
    for v in parts[1:]:
        try:
            marks.append(int(v))
            count = count + 1
        except:
            pass

    avg_marks = sum(marks) / count
    students[name] = avg_marks

for name, avg in sorted(students.items()):
    print(f"{name:20} {avg:6.2f}")

f.close()
