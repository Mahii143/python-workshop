N = int(input())

while N>0:

    if N%10 == 0:
        print('Duck Number')
        break
    N //= 10

if N == 0:
    print('Not a Duck Number')



