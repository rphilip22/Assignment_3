portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}

total_value = 0

for stock in portfolio:
    shares = portfolio[stock]["shares"]
    price = portfolio[stock]["price"]
    value = shares * price
    total_value += value

print("Total Portfolio Value:", total_value)

import random

print("\nSimulating 1 week of price changes:\n")

for day in range(1, 8):
    print("Day", day)

    for stock in portfolio:
        change_percent = random.uniform(-0.05, 0.05)
        portfolio[stock]["price"] *= (1 + change_percent)

    total_value = 0

    for stock in portfolio:
        shares = portfolio[stock]["shares"]
        price = portfolio[stock]["price"]
        stock_value = shares * price
        total_value += stock_value
        print(f"{stock}: shares = {shares}, price = ${round(price, 2)}, value = ${round(stock_value, 2)}")


    print("Total Portfolio Value: $", round(total_value, 2))
    print()