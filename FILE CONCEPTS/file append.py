file = open("File1.txt", "a+")
file.write("\n Python is good")
print("Data appended successfully")
file.close()
file = open("File1.txt", "r")
print(file.read())
file.close()
print("open and read completed...")
file = open("File1.txt", "r")
for line in file:
    print(line)