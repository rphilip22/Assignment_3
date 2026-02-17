loan_amt = float(input("Enter the loan amount: "))
monthly_pay = float(input("Enter the monthly payment: "))
rate = float(input("Enter the interest rate (in %): "))

monthly_rate = rate / 100 / 12
balance = loan_amt
months = 0
total_interest = 0

if monthly_pay <= balance * monthly_rate:
    print("Payment too low! Loan will never be paid off.")
    exit()

while balance > 0:
    interest = balance * monthly_rate
    balance = balance + interest - monthly_pay
    months += 1
    total_interest += interest

    if balance > 0:
        print("Remaining balance:", round(balance, 2))

print("Loan paid off in", months, "months with $", round(total_interest, 2), "paid as interest.")