# commissions.py
# Exercise 4: Sales Commission Leaderboard
# Uses a function for 10% commission and prints a ranked leaderboard.

# Hardcoded sales data dictionary
sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

# Function to calculate 10% commission on a given sales amount
def calculate_commission(sales_amount):
    return sales_amount * 0.10

# Build a list of (name, sales, commission) tuples
results = []
for name in sales:
    commission = calculate_commission(sales[name])
    results.append((name, sales[name], commission))

# Sort results by sales descending (manual bubble sort for clarity)
for i in range(len(results)):
    for j in range(i + 1, len(results)):
        if results[j][1] > results[i][1]:
            results[i], results[j] = results[j], results[i]

# Print the leaderboard
print("=== Sales Commission Leaderboard ===")
print("")
rank = 1
for entry in results:
    name = entry[0]
    total_sales = entry[1]
    commission = entry[2]
    print("Rank " + str(rank) + ": " + name +
          " | Sales: $" + str(total_sales) +
          " | Commission: $" + str(round(commission, 2)))
    rank = rank + 1
