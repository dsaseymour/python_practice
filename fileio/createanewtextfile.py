output_file=open("hello.txt", "w") #create a new text file 
#open returns a file object that is in output_file
output_file.writelines("This is my first file. \n")
lines_to_write=[
"This is my file \n",
"There are many like it ",
"but this one is mine \n"
]
output_file.writelines(lines_to_write)
output_file.close() #close the stream

output_file=open("hello.txt","a")
output_file.writelines("\nNON SEQUITUR")
output_file.close()



