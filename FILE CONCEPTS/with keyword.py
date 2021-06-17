with open("FileMahi.txt", "w") as file:
    file.writelines("Hi da")

file.close()


with open("FileMahi.txt", "r") as file:
    print(file.read())
file.close()

with open("FileMahi.txt", "a+") as file:
    file.write("\nEpdi iruke")
file.close()

with open("FileMahi.txt", "r") as file:
    for line in file:
        print(line, end=" ")
