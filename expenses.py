total = 0
expenses = {
    "Travel": [],
    "Meals": [],
    "Supplies": []
}

for category in expenses:
    while True:
        amount = float(input(f"Enter the amount for {category} (enter '0' to finish): "))
        if amount == 0:
            break
        expenses[category].append(amount)
        total += amount

print("\nExpense Summary Report:")
for category in expenses:
        print(f"Current total for {category}: ${sum(expenses[category]):.2f}")
print(f"Grand total: ${total:.2f}")