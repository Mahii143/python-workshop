numList = []
for num in list(map(int,input().split())):
    numList.append(num)

X = int(input())
print(numList[-X])
