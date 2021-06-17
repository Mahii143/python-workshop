N = int(input())

a = []
for j in range(N):
    a.append(int(input()))

if N%2 == 0:
    temp = [a[i]+a[i+1] for i in range(0,N,2)]

    for sums in temp:
        print(sums, end=  " ")
        
else:
    temp = [a[i]+a[i+1] for i in range(0,N-1,2)]
    
    for sums in temp:
        print(sums, end=  " ")

    print(a[-1])
