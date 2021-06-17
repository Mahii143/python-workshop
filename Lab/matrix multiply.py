R = int(input())
C = int(input())

m1 = []
for i in range(R):
    m1.append([int(val) for val in input().split()])

m3 = []
for i in range(C):
    m3.append([int(val) for val in input().split()])


print(len(m1))
print(len(m3[0]))
print(len(m3))

result = []
for i in range(R):
    row = []
    for j in range(R):
        row.append(0)
    result.append(row)


for i in range(len(m1)): 
  
    # iterating by coloum by B  
    for j in range(len(m3[0])): 
  
        # iterating by rows of B 
        for k in range(len(m3)): 
            result[i][j] += m1[i][k] * m3[k][j] 

for i in result:
    print(*i)
