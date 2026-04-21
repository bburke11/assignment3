# expenses.py
# Exercise 3: Expense Report
# Loops through a nested expenses dictionary and prints category totals and a grand total.

# Hardcoded expenses dictionary: categories map to lists of amounts
expenses = {
    "Travel":   [450.00, 320.50, 85.00, 200.00],
    "Meals":    [32.50, 48.75, 19.90, 55.00, 27.30],
    "Supplies": [112.00, 67.45, 34.99]
}

print("=== Expense Report ===")
print("")

grand_total = 0  # Running grand total across all categories

# Loop through each category and its list of amounts
for category in expenses:
    category_total = 0
    for amount in expenses[category]:
        category_total = category_total + amount  # Sum each amount in the category
    grand_total = grand_total + category_total
    print(category + " Total: $" + str(round(category_total, 2)))

print("")
print("Grand Total: $" + str(round(grand_total, 2)))
