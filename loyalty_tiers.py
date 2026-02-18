customers = {}

# Collect customer data until the user decides to stop
while True:
    name = input("Enter customer name (or 0 to finish): ")

    if name == "0":
        break

    amount = float(input("Enter total purchase amount: "))
    customers[name] = amount

bronze = 0
silver = 0
gold = 0

# Classify customers into tiers based on their purchase amounts
for customer in customers:
    amount = customers[customer]

    if amount < 1000:
        bronze += 1
    elif amount < 5000:
        silver += 1
    else:
        gold += 1

print("\nCustomer Tier Summary:")
print("Bronze:", bronze)
print("Silver:", silver)
print("Gold:", gold)
