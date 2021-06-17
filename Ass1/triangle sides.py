A,B,C = map(int,input().split())

if (A < B+C) and (B < A+C) and (C < A+B):
    print("The given numbers can form the sides of a triangle")

else:
    print("The given numbers cannot form the sides of a triangle")
