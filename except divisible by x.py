n , x = [int(val) for val in input().split()]

ctr = 1

while ctr <= n:
    if ctr%x == 0:
       ctr = ctr+1
       continue
    print(ctr, end = " ")

    ctr += 1
