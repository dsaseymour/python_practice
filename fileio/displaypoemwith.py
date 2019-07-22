import os.path

path = "C:/Users/Danny/Documents/python_practice/fileio/practice_files"

with open(os.path.join(path, "poem.txt")) as poem_source:
    for line in poem_source.readlines():
        print(line + "\n")
