try:
    n = int(input("Enter the numeber : "))
    if n >= 0:
        print(n)
    else:
        raise ValueError("Negative number is not allowed")
except ValueError as e:
    print(e)
