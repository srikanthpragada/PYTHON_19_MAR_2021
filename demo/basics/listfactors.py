# Print factors for the number given on command line
import sys

if len(sys.argv) < 2:
    print("Usage : python listfactors.py [-h] <number>")
    exit()

number_pos = 1
vertical = True
if sys.argv[1].upper() == '-H':
    vertical = False
    number_pos = 2
    if len(sys.argv) < 3:
        print("Usage : python listfactors.py [-h] <number>")
        exit()

num = int(sys.argv[number_pos])
for n in range(2, num // 2 + 1):
    if num % n == 0:
        if vertical:
            print(n)
        else:
            print(n, end=' ')
