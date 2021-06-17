file = open("File1.txt", "w")
file.write("Hello all, hope you are enjoying")
file.close()
print("writing was completed")

file  = open("File1.txt", "r")
print(file.readline())

