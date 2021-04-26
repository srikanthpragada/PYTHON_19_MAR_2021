# Print name and avg marks from marks.txt

f = open("marks.txt", "rt")
for line in f.readlines():
    parts = line.split(",")
    if len(parts) < 2:
        continue  # Ignore line and move to next line

    name = parts[0]
    try:
        marks = [int(v) for v in parts[1:]]
        avg_marks = sum(marks) / len(marks)
        print(f"{name:20} {avg_marks:3}")
    except:
        pass

f.close()
