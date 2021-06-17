''' Q5:Define file and Filepath.Write a program that reads a file
and copies its content in another file.While copying,replace all full stop with commas.{}
'''


with open("input2.txt") as f:
    with open("copiedfile.txt","w") as f2:
        buf = f.read()
        f2.write(buf)

f.close()
f2.close()

with open("copiedfile.txt","r") as f2:
    file_contents = f2.read()
    file_contents = file_contents.replace('.',',')

f2.close()

with open("copiedfile.txt","w") as f2:
    f2.write(file_contents)

f2.close()

with open("copiedfile.txt","r") as f2:
    print(f2.read())
print("File copied Successfully")

f2.close()




