N = int(input())
a= []
i = 0

for ctr in range(N):

    a.append(int(input()))

while i < N:

    if i+2 < N:

        product = a[i]*a[i+1]*a[i+2]

        print(product, end= " ")

    elif i+1 < N:

        product = a[i]*a[i+1]

        print(product, end= " ")

    else:

        print(a[i])


    i += 3
