# List all python file (.py) from parent directory
import os

allfiles = os.walk(r"d:\classroom\mar19\demo")  # Parent directory
for dirname, directories, files in allfiles:
    for filename in files:
        if filename.endswith(".py"):
            print( dirname + "\\" + filename)
