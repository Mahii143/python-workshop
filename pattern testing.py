N = int(input())

odd = 1

for i in range(1, N+1):

    for j in range(N - i):
        print(" ",end= " ")

    k = 0

    for j in range(1,odd+1):
        if j<= i:
           k += 1
        else:
            k -= 1

        print(k, end= " ")

    print()

    odd += 2
