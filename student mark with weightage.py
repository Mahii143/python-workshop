'''37.5
19.8
26.7'''

print(37.5+19.8+26.7)
exam1 = int(input("Enter the mark of Exam 1= "))
exam2 = int(input("Enter the mark of Exam 2= "))
tot1 = exam1 + exam2
average1 = tot1/2
percentage1 = average1*(30/100)

activity1 = int(input("Enter the mark of Activity 1= "))
activity2 = int(input("Enter the mark of Activity 2= "))
activity3 = int(input("Enter the mark of Activity 3= "))
tot2 = activity1 + activity2 + activity3
average2 = tot2/3
percentage2 = average2*(30/100)

sports1 = int(input("Score in Sports= "))
percentage3 = sports1*(20/100)


print(percentage1+percentage2+percentage3)
