def addition(a,b):
    print("Sum of the values is = ",a+b)

def subtraction(a,b):
    print("Difference of the values is = ",a-b)

def multiplication(a,b):
    print("Product of the values is = ",a*b)

def division(a,b):
    print("Quotient of the values is = ",a/b)

def modulo_division(a,b):
    print("Product of the values is = ",a%b)

def floar(a,b):
    print("Quotient of the values is = ", a//b)

x, y= map(int,input("Enter 2 numbers :").split())

inp = input("Enter the operation symbol: ").strip()
inp = str(inp)

if inp == '+':

    addition(x,y)

elif inp == '-':

    subtraction(x,y)

elif inp == '*':

    multiplication(x,y)

elif inp == '//':

    floar(x,y)

elif inp == '%':

    modulo_division(x,y)

elif inp == '/':

    division(x,y)

else:
    print("Please enter a valid operation!")
