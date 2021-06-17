#print a tuple that only contains positive integers from a list of both positive and negative numbers


mylist = [1,2,3,4,5,6,-2,-4,-5,-9,-100]
newtuple = []

for positive in mylist:
    if positive > 0:
        newtuple.append(positive)
        
print(tuple(newtuple))



