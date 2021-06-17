#print sum of positive integers from given arguments


def sumofpos(*val):
    tot = 0
    for t in val:
        for i in t:
            if i > 0:
                tot += i
    print(tot)
    
val = 1, 2, 3, 10,35,45,-35,-45,-32,-10
sumofpos(val)

