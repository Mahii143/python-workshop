l1 = [1,2,3,4,5,6,7,3,5,1,6,7]
key1 = 6
x = len(l1)

def lin(list1, val, n):
    count = 0
    for i in list1:
        if val == i:
            count += 1
    return count

ans = lin(l1,key1,x)
print(ans)
