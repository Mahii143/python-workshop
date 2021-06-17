numList = []
for num in list(map(int,input().split())):
    numList.append(num)

x, y  = map(int,input().split())
print(x in numList and y not in numList)
