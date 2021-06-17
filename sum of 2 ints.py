N = int(input())
a = []
i  = 0
for ctr in range(N):
    val = int(input())
    a.append(val)

while i<N:
    if i+1<N:
        print(a[i]+a[i+1],end=" ")

    else:
        print(a[i],end=" ")

    i += 2
