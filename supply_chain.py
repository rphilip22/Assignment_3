warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
]

total_stock = {}

for warehouse in warehouses:
    inventory = warehouse["inventory"]

    for product in inventory:
        quantity = inventory[product]

        if product in total_stock:
            total_stock[product] += quantity
        else:
            total_stock[product] = quantity

print("Total Stock Across Supply Chain:")
for product in total_stock:
    print(product, ":", total_stock[product])