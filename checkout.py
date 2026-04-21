# checkout.py
# Exercise 1: Shopping Checkout
# Uses a while loop to collect item prices, then prints total, average, and count.

prices = []  # List to store item prices

print("=== Shopping Checkout ===")
print("Enter item prices one at a time. Enter 0 when done.")

# Keep asking for prices until the user enters 0
while True:
    entry = float(input("Enter item price (0 to finish): "))
    if entry == 0:
        break  # Exit loop when user enters 0
    prices.append(entry)  # Add price to the list

# Calculate summary statistics
if len(prices) > 0:
    total = sum(prices)
    average = total / len(prices)
    print("\n--- Receipt Summary ---")
    print("Number of items: " + str(len(prices)))
    print("Total cost:      $" + str(round(total, 2)))
    print("Average cost:    $" + str(round(average, 2)))
else:
    print("No items were entered.")
