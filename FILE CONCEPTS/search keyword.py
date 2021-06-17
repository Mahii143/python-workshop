filename = input("Enter filename ")
with open(filename,"w") as file:
    inp = input("Enter the sentance : ")
    file.writelines(inp)
    file.close()
with open(filename, "r") as file:
    text =file.read()
    letter = input("Enter the word : ")
    count = 0
    for char in text:
        if char == letter:
            count+= 1
print(letter, "appears", count, " times in file")
file.close()
