# loan_simulator.py
# Exercise 6: Loan Repayment Simulator
# Asks the user for loan details and simulates monthly repayment using a while loop.

print("=== Loan Repayment Simulator ===")
print("")

# Get loan details from the user
loan_amount   = float(input("Enter the loan amount ($): "))
annual_rate   = float(input("Enter the annual interest rate (e.g., 5 for 5%): "))
monthly_payment = float(input("Enter your monthly payment ($): "))

# Convert annual rate to monthly rate
monthly_rate = (annual_rate / 100) / 12

balance = loan_amount  # Remaining balance
months  = 0           # Month counter

print("")
print("Month  | Balance Start  | Interest  | Payment   | Balance End")
print("-" * 65)

# Simulate repayment month by month
while balance > 0:
    months = months + 1
    balance_start = balance
    interest = balance * monthly_rate          # Interest charged this month
    balance  = balance + interest              # Add interest to balance

    # Handle final partial payment
    if monthly_payment >= balance:
        actual_payment = balance
        balance = 0
    else:
        actual_payment = monthly_payment
        balance = balance - monthly_payment

    print(str(months).ljust(6) +
          " | $" + str(round(balance_start, 2)).ljust(13) +
          " | $" + str(round(interest, 2)).ljust(8) +
          " | $" + str(round(actual_payment, 2)).ljust(8) +
          " | $" + str(round(balance, 2)))

print("")
print("Loan paid off in " + str(months) + " month(s).")
