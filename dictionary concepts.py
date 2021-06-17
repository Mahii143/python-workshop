stud = {"mahir":[50,35,69,78],"karthi":[35,35,60,90],"jeevan":[90,85,75,92]}
marks = stud
tot = 0

for i,j in marks.items():
    tot = sum(j)
    marks[i] = tot

maximum = 0

for i,j in marks.items():
    if j > 0:
        maximum = j
        topper = i
print("Student names and their marks: ",marks)
print("The topper of the class is ", topper)
print("Scores obtained by ",  topper, " is ",maximum)
