n1 = [3,4]
n2 = [5,6]
n3 = n1+n2

for i in n3:
    fact = 1
    if (i == 0 or i ==1):
        print(1)

    else:
        for j in range(1,i+1):
            fact *= j

    print(fact, end= " ")
        
