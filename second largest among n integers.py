n = int(input())
a = []
for i in list(map(int,input().split())):
    a.append(i)

b = sorted(a)
x= set(b)
x = list(x)
x.sort()
print(x[-2])
