# portfolio.py
# Exercise 5: Stock Portfolio Tracker
# Loops through a hardcoded portfolio dict, prints total value,
# and simulates a week of random daily price changes.

import random

# Hardcoded stock portfolio: ticker -> {shares, price}
portfolio = {
    "AAPL": {"shares": 10, "price": 175.50},
    "TSLA": {"shares": 5,  "price": 245.80},
    "AMZN": {"shares": 3,  "price": 185.20}
}

print("=== Stock Portfolio ===")
print("")

total_value = 0

# Print each stock and its current value
for ticker in portfolio:
    shares = portfolio[ticker]["shares"]
    price  = portfolio[ticker]["price"]
    value  = shares * price
    total_value = total_value + value
    print(ticker + ": " + str(shares) + " shares @ $" + str(price) +
          " = $" + str(round(value, 2)))

print("")
print("Total Portfolio Value: $" + str(round(total_value, 2)))

# --- Bonus: Simulate 7 days of +-5% random daily changes ---
print("")
print("=== 7-Day Price Simulation (+-5% daily change) ===")
print("")

# Work with a copy of the prices
sim_prices = {}
for ticker in portfolio:
    sim_prices[ticker] = portfolio[ticker]["price"]

for day in range(1, 8):
    daily_total = 0
    print("Day " + str(day) + ":")
    for ticker in sim_prices:
        change_pct = random.uniform(-0.05, 0.05)  # Random change between -5% and +5%
        sim_prices[ticker] = sim_prices[ticker] * (1 + change_pct)
        value = portfolio[ticker]["shares"] * sim_prices[ticker]
        daily_total = daily_total + value
        print("  " + ticker + ": $" + str(round(sim_prices[ticker], 2)))
    print("  Portfolio Total: $" + str(round(daily_total, 2)))
    print("")
