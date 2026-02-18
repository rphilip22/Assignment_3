warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
]

total_stock = {}

# Calculate total stock across all warehouses
for warehouse in warehouses:
    inventory = warehouse["inventory"]

# Aggregate stock for each product
    for product in inventory:
        quantity = inventory[product]

# Update total stock for the product
        if product in total_stock:
            total_stock[product] += quantity
        else:
            total_stock[product] = quantity

# Print total stock for each product
print("Total Stock Across Supply Chain:")
for product in total_stock:
    print(product, ":", total_stock[product])
