# Takes names from user and writes them into names.txt

f = open("names.txt","wt")
while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break
    f.write(name + "\n")

f.close()
