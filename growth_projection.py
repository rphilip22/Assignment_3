initial_revenue = float(input("Enter initial revenue: "))
growth_rate = float(input("Enter annual growth rate (in %): "))

rate = growth_rate / 100
revenue = initial_revenue

print("\nYear | Revenue")
print("---------------")

for year in range(0, 11):
    print(year, "|", round(revenue, 2))
    revenue = revenue * (1 + rate)