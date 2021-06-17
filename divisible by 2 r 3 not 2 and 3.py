N = int(input())

i, count =2, 0
while count<N:
    if (i%2 == 0 or i%3 == 0) and not i%6 == 0:
            print(i)
            count += 1
    i  += 1
