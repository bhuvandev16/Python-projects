def show_balance():
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    global balance
    try:
        deposit_amt = float(input('Enter an amount to be deposited: '))
        if deposit_amt > 0:
            balance += deposit_amt
            print(f"${deposit_amt:.2f} deposited successfully!")
        else:
            print("Deposit amount must be positive.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def withdraw():
    global balance
    try:
        withdraw_amt = float(input('Enter an amount to be withdrawn: '))
        if withdraw_amt <= balance and withdraw_amt > 0:
            balance -= withdraw_amt
            print(f"${withdraw_amt:.2f} withdrawn successfully!")
        elif withdraw_amt > balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def quit_program():
    print("Thank you, have a nice day!")

balance = 0.0

while True:
    print('''*********************
   Banking Program   
*********************
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
*********************''')
    
    try:
        choice = int(input('Enter your choice (1-4): '))
        
        if choice == 1:
            show_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            quit_program()
            break
        else:
            print("Please enter a valid option (1-4).")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
