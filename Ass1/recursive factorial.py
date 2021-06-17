n1 = [3,4]
n2 = [5,6]
n3 = n1+n2

def fact(n):

    if (n == 0 or n== 1) :
        return 1
    else:
        return n*fact(n-1)


for i in n3:
    ans = fact(i)

    print(ans, end= " ")
