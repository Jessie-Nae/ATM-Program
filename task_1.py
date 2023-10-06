#TASK---CREATING AN ATM PROGRAM
'''
Creating this I followed these steps:
    $defined a users account balance
    $printed a welcome message using a print function.
    $printed a list options to choose from requesting an input from the user .
        #withdraw
            #subtracts from the account balance/give an insufficient balance message
        #check balance
        #transfer
    $evaluates the user input using the conditional statement(s)    

'''
def atmProgram():
    account_balance = 100000

    print("Welcome,what would you like to do?")

    print("Enter: \n'W' to Withdraw \n'C' to Check_balance \n'T' to Transfer")

    user_entry = input(">>")
    user_entry.lower()

    if user_entry == 'w':
        withdrawal_amount = int(input("Withdrawal amount:"))
        if withdrawal_amount <= account_balance:
            remaining_balance = account_balance - withdrawal_amount
            print("Withdrawal successful \nCurrent account balance :", remaining_balance)
        else:
            print("Insufficient balance.")    
    elif user_entry == 'c':
        print("Your current balance is :",account_balance)

    elif user_entry == 't':
        print("Will be with you in a sec.")


atmProgram()


























