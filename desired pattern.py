'''a = [int(val) for val in input().split()]

for i in range(len(a)-1):
    if a[i]< a[i+1]:
        print(a[i], end= " ")

print(a[-1])

a  = int(input())
b = []
for i in range(a):
    b.append(str(input()))

b[0],b[-1] = b[-1], b[0]

print(*b)


'''
a, b = input().split()
a, b = int(a), str(b)

for i in range(ord("a"),ord(b)+1):
    for j in range(1,a+1):   #inthe line le change
        print(str(j)+(chr(i)), end= " ")
    print()
