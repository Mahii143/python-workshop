r,c = map(int,input().split())
rowmatrix = []
colmatrix = []
for j in range(r):
    a = []
    for i in list(map(int,input().split())):
        a.append(i)

    rowmatrix.append(a)
print("rowmat", rowmatrix)

for i in range(r):
    a = []
    for j in range(c):
        a.append(rowmatrix[j][i])

    colmatrix.append(a)
print("colmat", colmatrix)

#CHECK ROW

#zeros count in rows:
'''
for i in range(r):
    count = 0
    for j in range(c):
        if matrix[i][j] == 0:
            count += 1

    for i in range(c):
        count1 = 0
        for j in range(r):
            if matrix[j][i] == 0:
                count1 += 1
        print(count1)
    print(count)
'''
