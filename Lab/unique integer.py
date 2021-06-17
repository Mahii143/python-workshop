a = ["1 ","2 " ,"3 ","3 " ,"4 ","6 ","6 ","7 ","9 "]
a1 = [1,2,34,5,6,6,7]
f = open("input.txt", 'w')
f.writelines(a)
f.close()
f = open("input.txt",'r')
h = f.readlines()
d = map(int,*h)
print(d)
f.close()
