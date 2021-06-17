#a = [map(int,input().split()) for val in a if val%2 != 0]
#print(val)

'''cases = [input().split() for _ in range(input())]
flatList = [int(item) for elem in cases for item in elem]
print(flatList)
'''

lst1 = [int(val) for val in input("Enter the list items : ").split() if int(val)%2 != 0]
print(*lst1)
