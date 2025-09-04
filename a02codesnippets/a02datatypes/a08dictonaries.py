inventory = {
    "apple": 10,
    "banana": 25,
    "orange": 15
}

# items() - Loop through all items (key-value pairs)
print("Current Inventory:")
for item, quantity in inventory.items():
    print(f"{item.title()}: {quantity}")

# Inventory dictionary
inventory = {
    "apple": 10,
    "banana": 25,
    "orange": 15
}

# Check if an item is in inventory
item_to_check = "banana"

if item_to_check in inventory:
    print(f"{item_to_check.title()} is available with quantity {inventory[item_to_check]}.")
else:
    print(f"{item_to_check.title()} is not available in inventory.")



# keys() - Get all the item names
print("\nAvailable items in stock:")
print(list(inventory.keys()))

# values() - Get all the quantities
print("\nQuantities in stock:")
print(list(inventory.values()))

# update() - Add new items or update existing ones
new_stock = {
    "banana": 30,       # updating quantity
    "grapes": 50        # new item
}
inventory.update(new_stock)

print("\nUpdated Inventory:")
for item, quantity in inventory.items():
    print(f"{item.title()}: {quantity}")
