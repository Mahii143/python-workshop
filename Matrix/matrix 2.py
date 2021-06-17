r, c = [int(val) for val in input().split()]

matrix = []

for i in range(r):
    matrix.append([int(val) for val in input().split()])
#print(matrix)

tot  = 0

for i in range(r):
    for j in range(c):
        rowcount = 0
        if matrix[i][j] == 0:
            rowcount += 1

    if rowcount == 1:
        for j in range(c):
            for i in range(r):
                colcount = 0
                if matrix[i][j] == 0:
                    colcount += 1

            if rowcount == colcount:
                tot += 1
print(tot)

    
