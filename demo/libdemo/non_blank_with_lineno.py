# Display nonblank lines with line numbers

f = open("test.txt","rt")

for lineno, line in enumerate(f.readlines(),start=1):
    line = line.strip()
    if len(line) > 0:
        print(f"{lineno:3}: {line}")

# f.seek(0, whence=0)
f.close()