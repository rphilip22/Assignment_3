initial_revenue = float(input("Enter initial revenue: "))
growth_rate = float(input("Enter growth rate (in %): "))

rate = growth_rate / 100
revenue = initial_revenue

print("\nStartup Revenue Projection (ASCII Chart)\n")

for year in range(0, 6):
    bars_count = int(revenue / 500)

    if bars_count == 0 and revenue > 0:
        bars_count = 1

    bars = "#" * bars_count
    print("Year", year, ":", bars)

    revenue = revenue * (1 + rate)