N = int(input())
a = []

for ctr in range(N):
    a.append(int(input()))

if N%3 != 0:

    if N%3 == 2:
        
        temp = [(a[i]*a[i+1]*a[i+2]) for i in range(0,N-2,3)]

        for total in temp:
            print(total, end= " ")

        print(a[-1]*a[-2])

    elif N%3 == 1:

        temp = [(a[i]*a[i+1]*a[i+2]) for i in range(0,N-2,3)]

        for total in temp:
            print(total, end= " ")

        print(a[-1])


else:
    temp = [(a[i]*a[i+1]*a[i+2]) for i in range(0,N,3)]

    for total in temp:
        print(total, end= " ")

