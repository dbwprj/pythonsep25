# Creating a dictionary
product_prices = {
    "apple": 140,
    "banana": 8,
    "orange": 15
}

# Accessing values by key
print("Price of apple:", product_prices["apple"])

#  Adding a new item
product_prices["grape"] = 30
print("Added grape:", product_prices)

#  Modifying a value
product_prices["banana"] = 10
print("Updated banana price:", product_prices)

#  Removing an item
del product_prices["orange"]
print("After removing orange:", product_prices)

#  Looping through dictionary
print("\nProduct Price List:")
for product, price in product_prices.items():
    print(f"{product.title()} - Rs{price:.2f}")
