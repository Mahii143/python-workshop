N = int(input())

oddSum = 0

while N>0:

    if N%10%2 != 0:

        oddSum += N%10

    N //= 10

print(oddSum)
