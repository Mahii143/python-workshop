numList = []
for num in list(map(int,input().split())):
    numList.append(num)

y  = int(input())
print(*(numList[:(len(numList)-y)]), sep=" ")
