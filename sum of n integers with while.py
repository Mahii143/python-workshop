n = int(input('Enter the number of values: '))

sum = 0
count = 1

while n>0:
    sum += count

    count+= 1
    
    n -= 1

print(sum)


m = int(input('Enter the number of values: '))

sum = 0

for i in range(1,m+1):
    sum += i

print(sum)
