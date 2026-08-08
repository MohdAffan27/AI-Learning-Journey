# ATM SIMULATOR
# format of dict {pin: [username,balance]}
user_db = {
    "1234":["Affan" ,5000.0],
    "5678":["Bilal", 6000.0],
    "9101":["Junaid" ,7000.0]
}
print("----welcome to the ATM SIMULATION----")

# PIN VERIFICATION
entered_pin = input("Enter your PIN : ")

if entered_pin in user_db:
    # fetch data of the user using the entered pin as key 
    user_info = user_db[entered_pin]
    user_name = user_info[0]
    balance = user_info[1]

    print("\n Welcome Back", user_name)
    print("\n====Select the Service you want====")
    print("\n1 . Balance Enquiry")
    print("\n2 . Deposit")
    print("\n3 . Withdraw amount")
    print("\n4 . Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":
        print("\n",user_name,"Your account balance :",balance)
        print("Thank you for using this ATM!...visit again.")
    elif choice == "2":
        deposit = float(input("Enter Amount to deposit"))
        if deposit > 0:
            balance += deposit
            # Update balance int the Dictionary
            user_db[entered_pin][1]= balance
            print("Balance Deposited Sucessfully!")
            print("Your updated balance",balance)
            print("Thank you for using this ATM!...visit again.")
        else:
            print("Invalid amount entered")
            print("Thank you for using this ATM!...visit again.")
    elif choice == "3":
        withdraw = float(input("Enter Amount to withdraw : "))
        if withdraw >balance:
            print("Insufficient balance...check balance and try again")
            print("Thank you for using this ATM!...visit again.")
        elif withdraw <= 0:
            print("Invalid amount entered! try again")
            print("Thank you for using this ATM!...visit again.")
        else:
            balance -=withdraw
            # Update balance int the Dictionary
            user_db[entered_pin][1]=balance
            print("Balance withdrawn Sucessfully!")
            print("\nYour updated balance",balance)
            print("\nThank you for using this ATM!...visit again.")
    elif choice == "4":
        print("Thank you for using this ATM!...visit again.")
    else:
        print("Invalid key Entered, Try again")
        print("Thank you for using this ATM!...visit again.")
else:
    print("Password Invalid...access Denied!")
    print("Thank you for using this ATM!...visit again.")