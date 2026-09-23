# CodeAlpha Python Programming Internship
# Task 2: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("=" * 50)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

print("\nEnter your stock details.")
print("Type 'done' when you have finished.\n")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name. Please choose from the available stocks.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

        print(f"{quantity} shares of {stock_name} added successfully.\n")

    except ValueError:
        print("Please enter a valid whole number for quantity.\n")


print("\n" + "=" * 50)
print("             YOUR PORTFOLIO")
print("=" * 50)

if len(portfolio) == 0:
    print("No stocks were added.")
else:
    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Value':<12}")
    print("-" * 46)

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = quantity * price
        total_investment += value

        print(f"{stock:<10}{quantity:<12}${price:<11}{value:<12}")

    print("-" * 46)
    print(f"Total Investment: ${total_investment}")

print("=" * 50)
print("Thank you for using Stock Portfolio Tracker!")
print("=" * 50)