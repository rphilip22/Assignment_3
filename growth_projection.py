initial_revenue = float(input("Enter initial revenue: "))
growth_rate = float(input("Enter annual growth rate (in %): "))

rate = growth_rate / 100 # Convert percentage to decimal
revenue = initial_revenue

print("\nYear | Revenue")
print("---------------")

# Loop through 10 years and calculate the projected revenue
for year in range(0, 11):
    print(year, "|", round(revenue, 2))
    revenue = revenue * (1 + rate)
