n, m  = map(int,input().split())

def hcf(a,b):
    if b == 0:
        return a
    else:
        return hcf(b, a%b)

ans = hcf(n,m)
print(ans)


N = int(input())
list1 = [int(val) for val in input().split()]
z = hcf(list1[0], list1[1])

if N== 2:
    print(z)

else:
    for i in range(len(list1)):
        z  = hcf(z,list1[i])

    print(z)
