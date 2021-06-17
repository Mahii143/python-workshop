def bank_loan():    #defining a function called bank_loan

    def loop():

        print("continue -1 or end - 0")

        n =input()

        if n == '1':

            bank_loan()

        elif n == '0':

            print("Bye....")

        else:

            print("Enter either 0 or 1")

            loop()
            
    
    def eligible():

        '''This function used to execute the final output'''

        print("Account number : ",account_number)

        print("Eligiblity : Eligible")

        print("Requested Loan amount : ",loan_amount_expected)

        print("Expected No. of EMI's :",customer_emi_expected)


    account_number = int(input("Enter your 4 digit bank account number: ")) #account number of the user

    account_number = str(account_number)  #to perform len function we have to convert int to str

    if len(str(account_number)) != 4 or (str(account_number)[0]) != '1':  #the account numeber should be 4 digits and the first digit must be 1

            print("Please enter a valid account number")

            loop()

    else:

        account_balance = int(input("Enter your account balance: ")) #account balance of the user

        if account_balance < 100000:   #account balance should be greater than 1 lakh
            
            print("Sorry, your account balance isn't qualify the requirements for loan transactions!")

            loop()

        else:
            
            salary = int(input("Enter your monthly salary: "))  #salary of the user

            if salary < 25000: #minimum salary is 25000

                print("Sorry, your salary isn't qualify the requirements for loan transactions")

                loop()

            else:
                
                print("Available Loan Types : Car, House, Business")  #available loan types

                loan_type = input('Enter the loan type: ')

                loan_type_list = ['Car','car','House','house','Business','business'] #list of loan types in capitalised and un capitalised

                if (loan_type not in loan_type_list): #user entered loan type should be in list of loan types

                    print('Please enter a valid loan type')

                    loop()

                else:

                    loan_amount_expected = int(input("Enter your expected loan amount: "))  #loan amount expectation of user

                    customer_emi_expected = int(input("Enter your expected EMI: "))   #No. of EMI's expected by user

                    if loan_type == "Car" or loan_type == 'car':  #car loan requirements

                        if salary >= 25000:
                                

                            if loan_amount_expected <= 500000:

                                if customer_emi_expected <= 36:

                                    eligible()

                                else:

                                    print("Expected EMI is higher than eligible EMI, please choose 36 or less.")

                                    loop()

                            else:

                                print("Expected loan amount is higher than eligible loan amount, please choose 500000 or less.")

                                loop()

                        else:

                            print("Sorry, your salary isn't qualify the requirements for loan transactions")

                            loop()
                            

                    elif loan_type == "House" or loan_type == 'house':  #house loan requirements

                        if salary >= 50000:

                            if loan_amount_expected <= 6000000:

                                if customer_emi_expected <= 60:

                                    eligible()

                                else:

                                    print("Expected EMI is higher than eligible EMI, please choose 60 or less.")

                                    loop()

                            else:

                                print("Expected loan amount is higher than eligible loan amount, please choose 6000000 or less.")

                                loop()

                        else:

                            print("Sorry, your salary isn't qualify the requirements for loan transactions, try car loan")

                            loop()

                    elif loan_type == "Business" or loan_type == 'business': #business loan requirements

                        if loan_amount_expected <= 7500000:

                            if salary >= 75000:
                                    

                                if customer_emi_expected <= 84:

                                    eligible()

                                else:

                                    print("Expected EMI is higher than eligible EMI, please choose 84 or less.")

                                    loop()

                            else:

                                print("Expected loan amount is higher than eligible loan amount, please choose 7500000 or less.")

                                loop()

                        else:

                            print("Sorry, your salary isn't qualify the requirements for loan transactions, try car loan or house loan")

                            loop()

bank_loan()


