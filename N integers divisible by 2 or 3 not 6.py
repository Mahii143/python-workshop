n, x, y = map(int,input().split())

printVal = 2

while n>0:
    if (printVal%x == 0 or printVal%y ==0) and (printVal%(x*y) != 0):
        print(printVal, end = " ")

        n -= 1

    printVal += 1
