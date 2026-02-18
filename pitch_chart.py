initial_revenue = float(input("Enter initial revenue: "))
growth_rate = float(input("Enter growth rate (in %): "))

rate = growth_rate / 100
max_revenue = 0
revenue = initial_revenue

print("\nStartup Revenue Projection (ASCII Chart)\n")

for year in range(0, 6):
    max_revenue = revenue * (1 + rate)

for year in range(0, 6):
    bars_count = int(revenue / max_revenue * 5) if max_revenue > 0 else 0 
    # Calculate the number of bars to represent the revenue, scaled to a maximum of 5 bars

    bars = "#" * bars_count
    print("Year", year, ":", bars, round(revenue, 2)) # Print the year and the corresponding bars representing the revenue

     # Update revenue for the next year based on the growth rate
    revenue = revenue * (1 + rate)
