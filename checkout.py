prices = []  # empty list to store item prices
total = 0.0  # variable to keep track of total purchase amount

while True:
    price = float(input("Enter item price (0 to finish): "))

    if price == 0:
        break  # stop the loop

    if price < 0:
        print("Invalid price. Please enter a positive number.")
        continue  # skip and ask again

    prices.append(price)  # add price to list
    total += price

# After loop ends
if len(prices) > 0:
    average = total / len(prices)

    print("Total purchase amount:", total)
    print("Average item cost:", average)
    print("Number of items bought:", len(prices))
else:
    print("No items were purchased.")