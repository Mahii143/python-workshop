num = [int(val) for val in input().split()]
index = 0
while True:
    if num[index] %5 == 0:
        break
    print(num[index], end= " ")
    index += 1
