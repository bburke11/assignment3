# survey.py
# Exercise 2: Survey Preference Counter
# Uses a for loop and dictionary to count preferences and print market-share percentages.

# Hardcoded list of survey responses
responses = ["coffee", "tea", "coffee", "soda", "tea", "coffee", "soda", "coffee", "tea", "soda"]

counts = {}  # Dictionary to hold preference counts

# Count each preference using a for loop
for item in responses:
    if item in counts:
        counts[item] = counts[item] + 1  # Increment existing count
    else:
        counts[item] = 1  # Initialize new preference

total_responses = len(responses)

print("=== Beverage Preference Survey Results ===")
print("Total responses: " + str(total_responses))
print("")

# Print each item with its market-share percentage
for beverage in counts:
    percentage = (counts[beverage] / total_responses) * 100
    print(beverage.capitalize() + ": " + str(counts[beverage]) + " votes (" + str(round(percentage, 1)) + "%)")
