import csv

# Sample stock price data (date, closing price)
stock_data = [
    ["Date", "Close Price"],
    ["2025-09-01", 150.25],
    ["2025-09-02", 152.30],
    ["2025-09-03", 148.75]
] #observe list of lists. what changes will you do if you convert this into a list of dictionaries.

# Writing to CSV file
with open("stock_prices.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(stock_data)

print("Data written to stock_prices.csv")

# Reading from CSV file
with open("stock_prices.csv", "r") as file:
    reader = csv.reader(file)
    print("\nReading stock prices from CSV:")
    for row in reader:
        print(row)
