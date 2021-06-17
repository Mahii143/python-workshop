n = [int(val) for val in input().split()]
'''p1, p2, p3, p4, p5 = map(int,input().split())
p1, p2, p3, p4, p4 = int(p1), int(p2), int(p3), int(p4), int(p5)
n = [p1,p2,p3,p4,p5]
'''
a = 0
for i in range(5):
    if n[i] <= ((sum(n))-n[i]):
        a += 1
    else:
        a -= 1

if a != 5:
    print("SPD Emergency")
else:
    print("Stable")
