file = open("File1.txt", "wb")
print("Name of the file is: ", file.name)
file.close()
print("File is closed.", file.closed)
print("File has been opened in: ", file.mode, "mode")
