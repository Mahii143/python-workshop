n = int(input())
a = [int(val) for val in input().split()]
prof = 0
harry = 0
for i in range(0,len(a),2):
    prof += i
for i in range(1,len(a),2):
    harry += i

if prof >= harry:
    print("Professor")

else:
    print("Harry")
