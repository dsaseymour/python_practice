import os.path
path = "C:/Users/Danny/Documents/python_practice/fileio/practice_files"

output_file=open("output.txt","w")
read_file=open( os.path.join(path, "poem.txt") ,"r")

for line in read_file.readlines():
        output_file.write(line)

output_file.close
read_file.close

append_file=open("output.txt","a")
append_file.write("\n This better be appended to the end of the file")