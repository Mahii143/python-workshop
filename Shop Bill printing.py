ItemName1 = str(input("ItemName-"))
Quantity1 = int(input("Quantity-"))
Price1 = int(input("Price-"))
ItemName2 = str(input("ItemName-"))
Quantity2 = int(input("Quantity-"))
Price2 = int(input("Price-"))
TotalPrice= (Quantity1*Price1)+(Quantity2*Price2)
print(format('*','*>25'),'BILL',format('*','*>25'))
print("ItemName\t\tQuantity\t\tPrice")
Firstline = "{0}\t\t\t{1}\t\t\t{2}"
print(Firstline.format(ItemName1,Quantity1,Price1))
Secondline = "{0}\t\t\t{1}\t\t\t{2}"
print(Secondline.format(ItemName2,Quantity2,Price2))
print(format('*','*>56'))
Total = "Total amound to be paid\t\t\t\t{}"
print(Total.format(TotalPrice))
print(format('*','*>56'))
