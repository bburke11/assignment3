# supply_chain.py
# Exercise 7: Supply Chain Inventory Aggregator
# Loops through a list of warehouse dicts, aggregates stock of each product.

# Hardcoded list of warehouses, each containing an inventory dictionary
warehouses = [
    {"name": "Warehouse A", "inventory": {"Widgets": 120, "Gizmos": 45, "Thingamajigs": 30}},
    {"name": "Warehouse B", "inventory": {"Widgets": 80,  "Gizmos": 90, "Doohickeys": 60}},
    {"name": "Warehouse C", "inventory": {"Widgets": 55,  "Thingamajigs": 70, "Doohickeys": 25}}
]

total_stock = {}  # Dictionary to accumulate totals across all warehouses

# Loop through each warehouse and its inventory
for warehouse in warehouses:
    for product in warehouse["inventory"]:
        qty = warehouse["inventory"][product]
        if product in total_stock:
            total_stock[product] = total_stock[product] + qty  # Add to existing total
        else:
            total_stock[product] = qty  # Initialize new product total

print("=== Supply Chain: Total Stock by Product ===")
print("")

# Print the aggregated totals
for product in total_stock:
    print(product + ": " + str(total_stock[product]) + " units")
