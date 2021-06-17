'''

Q8:  You must implement the function writeStringToFile which accepts a string S as the input.
The function must create a file called "output.txt". Then the function must write the string S to
the file "output.txt".{}
'''

def writeStringToFile():
    S = input().strip()
    file = open("output.txt",'w')
    file.write(S)
    file.close()

    file = open("output.txt")
    print(file.readline())


writeStringToFile()













