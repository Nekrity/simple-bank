# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# Datu tipi, mekle float - https://www.w3schools.com/python/python_datatypes.asp
# Pārbaudēm izmanto if...else - https://www.w3schools.com/python/python_conditions.asp
# Cipari https://www.w3schools.com/python/python_numbers.asp
# 

balance = 0

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        deposit=int(input("How much do you want to deposit?"))
        if (deposit > 0):
            balance=balance + deposit
        elif(deposit <= 0):
            print("Invalid value! Value cannot be zero or negative")
        else:
            print("Enter only numbers")
        pass
    elif choice == '2':
        withdraw=int(input("How much do you want to withdraw?"))
        if (withdraw<=0):
            print("Invalid value! Value cannot be zero or negative")
        elif(withdraw>balance):
            print("You don't have enough money on your balance")
        else:
            balance=balance - withdraw
        pass
    elif choice == '3':
        print("Your current balance:", balance)
        pass
    elif choice == '4':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
