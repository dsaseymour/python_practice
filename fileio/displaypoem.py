import os.path

path = "C:/Users/Danny/Documents/python_practice/fileio/practice_files"

poem_source=open(os.path.join(path, "poem.txt"))
for line in poem_source.readlines():
    print(line + "\n")

poem_source.close()