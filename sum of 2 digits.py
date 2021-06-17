N = str(input())

if len(N)%2 == 0:
    
    temp = [(int(N[i:i+2])) for i in range(0,len(N),2)]

    total = 0

    for i in temp:
        total += i

    print(total)

else:

    temp = [(int(N[i:i+2]))for i in range(0,len(N)-1,2)]

    total = 0

    for i in temp:
        total += i

    print(total)
