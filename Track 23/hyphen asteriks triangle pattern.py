n = int(input())
odd = 1
for i in range(n):
    for j in range(1,n-i):
        print("-", end = "")
    for j in range(0,odd):
        print("*", end = "")
    odd += 2
    for j in range(1,n-i):
        print("-", end = "")
    print()
