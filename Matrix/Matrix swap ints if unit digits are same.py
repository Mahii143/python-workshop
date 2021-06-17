R, C = map(int,input().split())

#get user matrix1
matrix1 = []
for i in range(R):
    rows = list(map(int,input().split()))
    for i in rows:
        matrix1.append(i)

#get user matrix2
matrix2 = []
for i in range(R):    
    rows = list(map(int,input().split()))
    for i in rows:
        matrix2.append(i)

#accessing the values of 2 matrices simultaneously
for i in range(R):
    for j in range(C):
        cur1 = matrix1[i+j] #assigning a variable for current value of matrix in matrix1
        cur2 = matrix2[i+j] #assigning a variable for current value of matrix in matrix2
        
        unitdig1 = cur1%10 #get the matrix1 value's unit digit
        unitdig2 = cur2%10 #get the matrix2 value's unit digit
        
        if unitdig1 == unitdig2: #check if both unit digits are same
            matrix1[i+j] = cur2 #insert the matrix2 value in matrix1 value position
            matrix2[i+j] = cur1 #insert the matrix1 value in matrix2 value position

#print final matrix 1

for j in range(0,len(matrix1),3):
    print(matrix1[j],matrix1[j+1],matrix1[j+2])

#print final matrix 2

for j in range(0,len(matrix2),3):
    print(matrix2[j],matrix2[j+1],matrix2[j+2])

