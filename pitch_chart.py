# pitch_chart.py
# Exercise 10: ASCII Revenue Bar Chart
# Uses nested loops and string multiplication to print a bar chart of projected revenue.

print("=== Projected Revenue Bar Chart ===")
print("")

# Starting revenue and growth rate (hardcoded)
initial_revenue = 100000   # $100,000 starting revenue
growth_rate     = 0.10     # 10% annual growth rate
scale           = 50000    # Each '#' represents $50,000

# Build a list of (year, revenue) tuples using a loop
projections = []
revenue = initial_revenue
for year in range(1, 11):
    revenue = revenue * (1 + growth_rate)
    projections.append((year, revenue))

# Print the bar chart using nested loops
# Outer loop: each year (one row per year)
for entry in projections:
    year    = entry[0]
    rev     = entry[1]
    # Inner loop: build the bar by repeating '#' based on scaled revenue
    bar_len = int(rev / scale)  # Number of # symbols
    bar     = ""  # Start with empty bar string
    for i in range(bar_len):
        bar = bar + "#"  # Append one '#' per unit
    # Print the row: year label, bar, and dollar value
    label = "Year " + str(year).rjust(2)
    print(label + " | " + bar + " $" + str(round(rev, 0)))

print("")
print("Scale: each # = $" + str(scale))
