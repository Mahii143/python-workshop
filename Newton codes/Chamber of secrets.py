a = [int(val) for val in input().split()]
b = [int(val) for val in input().split()]
c = 1000000007
val = 0
fib = a[1]
for i in range(a[0]):
    val = (fib//b[i])%c
    fib = val
print(fib)
