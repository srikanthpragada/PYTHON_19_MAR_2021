# Remove all blank lines from given file

import os

filename = "names.txt"
tempfile = "temp.txt"

sf = open(filename, "rt")
tf = open(tempfile, "wt")

for line in sf:
    line = line.strip()
    if len(line) > 0:
        tf.write(line + "\n")

sf.close()
tf.close()

# Delete actual file
os.remove(filename)
# Rename temp file to actual file
os.rename(tempfile, filename)
