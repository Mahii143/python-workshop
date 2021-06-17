#define a function called result 
#used to return final result if all requirements are met
def result():
    print("Account number: ",account_number)
    print("Loan Sanction: Eligible")
    print("Requested loan amount: ", loan_amount_expected)
    print("Requested EMI: ", customer_emi_expected)

#get user account number    
account_number = int(input("Enter 4 digit account number: "))
#check account no. is 4 digit and starts with 1
if len(str(account_number)) == 4 and (str(account_number))[0] == "1":
    #get user account balance
    account_balance= int(input("Your account balance: "))
    #check balance is greater than 1 lakh
    if account_balance >= 100000:    
            #get user salary
            salary = int(input("Your monthly salary: "))
            #check salary is greater than 25000
            if salary > 24999:
                    #list contains loan types
                    a = ["Car","car","House","house","Business","business"]
                    #get user loan type
                    loan_type = input("Expected loan type: ")
                    #check loan type is in the list
                    if loan_type in a:
                            #get user expected amount and emi
                            loan_amount_expected = int(input("loan amount expected: "))
                            customer_emi_expected = int(input("loan emi expected: "))
                            #check loan type, salary , expected amount and emi mets requirements
                            if loan_type == a[0] or loan_type == a[1]:
                                if salary > 24999 and loan_amount_expected <= 500000 and customer_emi_expected <= 36:
                                    #call result function
                                    result()
                                else:
                                    print("Your request cannot be accepted")

                            elif loan_type == a[2] or loan_type == a[3]:
                                if salary > 49999 and loan_amount_expected <= 6000000 and customer_emi_expected <= 60:
                                    result()
                                else:
                                        print("Your request cannot be accepted")

                            elif loan_type == a[4] or loan_type == a[5]:
                                if salary > 74999 and loan_amount_expected <= 7500000 and customer_emi_expected <= 84:
                                        result()
                                else:
                                        print("Your request cannot be accepted")

                    #error for invalid loan type
                    else:
                        print("Enter a valid loan type")

            #error for less salary
            else:
                print("Your salary doesn't met our requirements")

    #error for less balance
    else:
        print("Your account balance is less than 1 Lakhs")

#error for invalid account number 
else:
    print("Please enter a valid account number")
