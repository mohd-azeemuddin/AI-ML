balance = 500
user = input("Enter the operation you want to do (Check balance, Withdraw, Deposit): ").lower()
if user == "check_balance":
    print(f"Available balance: {balance}")
elif user == "withdraw":
    withdraw_amt = int(input("Enter the amount you want to withdraw: "))
    if withdraw_amt > balance:
        print("Sorry, no required balance")
    else:
        amt = balance - withdraw_amt
        print(f"Balance: {amt}")
elif user == "deposit":
    deposit = int(input("Enter the amount you want to deopsit: "))
    amt = balance + deposit
    print(f"Balance: {amt}")
else:
    print("Invalid option handling")

    


    
