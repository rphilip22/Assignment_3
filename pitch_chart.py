initial_revenue = float(input("Enter initial revenue: "))
growth_rate = float(input("Enter growth rate (in %): "))

rate = growth_rate / 100
revenue = initial_revenue

print("\nStartup Revenue Projection (ASCII Chart)\n")

for year in range(0, 6):
    bars_count = int(revenue / 1000) # Adjust the divisor for different scales of revenue

    if bars_count == 0 and revenue > 0:
        bars_count = 1 # Ensure that even small revenues are represented with at least one bar

    bars = "#" * bars_count
    print("Year", year, ":", bars) # Print the year and the corresponding bars representing the revenue

    revenue = revenue * (1 + rate) # Update revenue for the next year based on the growth rate

# NOTE: This will only work if the revenue is in the range of thousands. 
# Adjust the divisor in bars_count calculation for different scales.
# initial_revenue could be used as the divisor to make it more dynamic, but it may lead to very long bars for high initial revenues.
