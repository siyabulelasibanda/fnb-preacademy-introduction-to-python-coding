# Set the starting bank balance.
balance = 500

# Ask the user how much money they want to withdraw.
withdrawal = float(input("Enter withdrawal amount: R"))

# Check whether the withdrawal is valid and affordable.
if withdrawal <= 0:
    print("Invalid amount. You must withdraw more than R0.")
elif withdrawal <= balance:
    balance = balance - withdrawal
    print(f"Withdrawal successful! Remaining balance: R{balance}")
else:
    print("Declined. Insufficient funds")
