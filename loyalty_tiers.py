# loyalty_tiers.py
# Exercise 8: Customer Loyalty Tier Assignment
# Loops through customer purchase amounts and assigns Bronze, Silver, or Gold tiers.

# Hardcoded dictionary of customer names and total purchase amounts
customers = {
    "Alice":   4200,
    "Bob":     850,
    "Carol":   5500,
    "David":   1200,
    "Eve":     300,
    "Frank":   7800,
    "Grace":   999,
    "Hank":    3100
}

# Tier counters
bronze_count = 0
silver_count = 0
gold_count   = 0

print("=== Customer Loyalty Tiers ===")
print("")

# Assign tier based on purchase amount
for customer in customers:
    amount = customers[customer]
    if amount >= 5000:
        tier = "Gold"
        gold_count = gold_count + 1
    elif amount >= 1000:
        tier = "Silver"
        silver_count = silver_count + 1
    else:
        tier = "Bronze"
        bronze_count = bronze_count + 1
    print(customer + " ($" + str(amount) + "): " + tier)

print("")
print("--- Tier Summary ---")
print("Bronze: " + str(bronze_count) + " customer(s)")
print("Silver: " + str(silver_count) + " customer(s)")
print("Gold:   " + str(gold_count)   + " customer(s)")
