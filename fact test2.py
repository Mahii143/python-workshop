def fact(n):
    if n< 0:
        print("please enter valid number")
    elif n == 0 or n == 1:
        return 1
    else:
        return (n*fact(n-1))

x = 5
print(fact(x))
