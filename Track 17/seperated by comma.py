numList = []
for num in list(map(int,input().split())):
    numList.append(int(num))

print(*(numList[::1]), sep= ",")
