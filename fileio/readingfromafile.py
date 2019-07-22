input_file=open("hello.txt","r")
print(input_file.readlines())
input_file.seek(0)

for line in input_file.readlines():
    print(line)

input_file.close()
