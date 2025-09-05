# Basic setup
daily_sales = [250, 0, 400, 600, 300, 0, 800]  
cost_per_day = 200                             
target_profit = 1000                           
total_profit = 0

# List of item prices
prices = [10, 20, 15, 30, 25]

# Loop through the list
for price in prices:
    print(f"Item price: ${price}")



'''
It iterates over the list daily_sales, 
giving you both the index (day) and the
 value (sale) for each item.

enumerate() is a built-in Python function that adds a counter (i.e., an index) to an iterable (like a list).
start=1 tells Python to start counting from 1 instead of the default 0 (so Day 1, Day 2, etc.).
It returns pairs: (index, value) → in this case, (day, sale)

list(enumerate(daily_sales, start=1))
 [(1, 250), (2, 0), (3, 400), (4, 600), (5, 300), (6, 0), (7, 800)]

 This unpacks each tuple (day, sale) into two variables:

'''



# Loop over daily sales
for day, sale in enumerate(daily_sales, start=1):
    print(f"\nDay {day}:")

    # Skip the day if no sales
    if sale == 0:
        print("No sales today. Skipping...")
        continue

    # Arithmetic operators
    profit = sale - cost_per_day       # subtraction
    total_profit += profit             # += assignment operator

    # Comparison + if condition
    if profit > 0:
        print(f"Profit for the day: Rs {profit}")
    elif profit == 0:
        print("Break-even today.")
    else:
        print(f"Loss of Rs {-profit} today.")

    # Logical operators
    if profit > 300 and sale > 500:
        print("High performance day!")

    # Break if target met
    if total_profit >= target_profit:
        print("\n Target profit reached. Stopping early.")
        break

# Final summary
print("\n--- Weekly Summary ---")
print(f"Total Profit: Rs {total_profit}")
if total_profit >= target_profit:
    print(" Goal met!")
else:
    print("Goal not met. Keep pushing!")
