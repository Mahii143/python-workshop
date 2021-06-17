def sumofval(numbers):
    total = 0
    for i in numbers:
        if i > 0:
            total += i

    return total

n = 1,2,3,4,5,-132,-23
tot = sumofval(n)
print(tot)

