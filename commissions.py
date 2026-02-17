sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}
commission = {}

def calculate_commission(sales_amount):
    return sales_amount * 0.1
for salesperson, amount in sales.items():
    commission[salesperson] = calculate_commission(amount)
print("Salesperson Commissions:")

print("\nLeaderboard (Highest to Lowest):")

while commission:
    highest_person = None
    highest_commission = 0

    for salesperson in commission:
        if commission[salesperson] > highest_commission:
            highest_commission = commission[salesperson]
            highest_person = salesperson

    print(f"{highest_person}: ${highest_commission:.2f}")
    del commission[highest_person]