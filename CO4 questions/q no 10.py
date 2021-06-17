''' Q10: You must implement the function ''appendStringToFile'' which accepts two string values F and S.
F represents a filename and S represents a string. The program must open the file F
and append the string S with the existing content.
'''
#function defined to append user input string into an existing file 
def appendStringToFile(A, B):
    file = open(A, 'a')
    file.write(" ")
    file.write(B)
    
    file.close()

    file = open(A, "r")
    print(file.readline())


F = input().strip()
S = input().strip()

#called the function to append the string
a = appendStringToFile(F,S)


