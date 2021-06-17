a = list(map(int,input().split()))

b = []
c = []
for i in range((len(a)//2)):
    b.append(a[i])

for i in range(len(a)-1,(len(a)//2)-1,-1):
    c.append(a[i])
b.sort()
c.sort(reverse = True)
print(*b, end= " ")
print(*c)
