def bill():
   

    #total amount
    def total():
        print("Total amount: ",(plate*quantity+distance*charge),"-/.")

    #declare prices for veg and non veg
    veg = 120
    non_veg = 150
    charge = 0

    #get user input for food type
    food = input("Enter type of food (V/N): ")

    #if food type veg or non veg the prices differs
    if food == "V" or food == "N":
        if food == "V":
            plate = veg

        elif food == "N":
            plate = non_veg

        #get user input of quantity and delivery distance        
        quantity = int(input("How many plates you like to order: "))

        if quantity >= 1:
            distance =int(input("Delivery distance in Km : "))

            #charge for delivery distance differs
            if 0< distance <= 3:
                charge = 0
                total()

            elif 3 < distance <= 6:
                charge =3
                total()
                
            elif distance >6 :
                charge = 6
                total()

            #print error if distance is 0    
            else:
                error()
                
        #print error if quantity is less than 1
        else:
            error()

    #if any of the inputs are invalid then print -1
    else:
        error()
    

bill()
