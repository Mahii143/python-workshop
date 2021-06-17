def lin(l, k, n):
    count = 0
    for i in range(n):
        if l[i] == k:
            count += 1
    return (count)

N = int(input())
list1 = [int(val) for val in input().split()]
key = int(input())

ans = lin(list1,key,N)
print(ans)
