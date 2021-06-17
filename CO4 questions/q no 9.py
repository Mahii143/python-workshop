'''
You must implement the function removeOddLengthWords which accepts a string F denoting
the filename as the input. The file contains a string S with spaces.
Then the function must remove all the words having the length as odd in the file.{}
'''

def removeOddLength(A):

    file = open(A)
    words = file.readline()
    a = [str(val) for val in words.split()]
    file.close()

    #if the length of the word is odd it is being removed
    L = []
    for i in range(len(a)):
        if len(a[i])%2== 0:
            L.append(a[i])

    #Now the words with even length getting replaced to the content of file
    file = open(A,'w')
    for i in L:
        file.write(i)
        file.write(" ")
    file.close()

    #reading the file to get final output
    file = open(A)
    print(file.readline())
    file.close()    
F= input().strip()
a = removeOddLength(F)



