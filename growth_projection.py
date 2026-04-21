# growth_projection.py
# Exercise 9: Revenue Growth Projection
# Asks for initial revenue and growth rate, then projects year-by-year for 10 years.

print("=== Revenue Growth Projection ===")
print("")

# Get starting values from the user
initial_revenue = float(input("Enter initial annual revenue ($): "))
growth_rate     = float(input("Enter annual growth rate (e.g., 10 for 10%): "))

rate_decimal = growth_rate / 100  # Convert percentage to decimal

print("")
print("Year-by-Year Revenue Projection")
print("-" * 35)
print("Year  | Revenue")
print("-" * 35)

revenue = initial_revenue  # Start with the initial revenue

# Loop 10 years and apply the growth rate each year
for year in range(1, 11):
    revenue = revenue * (1 + rate_decimal)  # Apply growth rate
    print("Year " + str(year).ljust(4) + "| $" + str(round(revenue, 2)))

print("-" * 35)
print("Final Year 10 Revenue: $" + str(round(revenue, 2)))
