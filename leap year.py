Y = input()

unit = Y[-1]
tenth = Y[-2]
hundredth = Y[-3]

if len(Y)== 4:
    if int(tenth) == 0 and int(unit) == 0:
        print("no")

    elif int(Y)%4 != 0:
        print("no")

    elif int(Y)%4 == 0:
        print("yes")

else:

    if int(Y)%4 != 0:
        print("no")

    elif int(Y)%4 == 0:
        print("yes")
