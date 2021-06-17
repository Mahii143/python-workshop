def gcd(a,b):

    if b == 0:   #if the value of b is 0 then the other value is Great common divisor
        return a

    else:
        #if a = 4,b = 8
        #first output (8,0)
        #here the b value becomes zero, calling the function again will make the first condition True.
        #So it will return a there.
        return gcd(b,a%b)   

x, y = map(int,input().split())

GCD = gcd(x,y)

print(GCD)
