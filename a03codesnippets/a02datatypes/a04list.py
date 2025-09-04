#  Creating a list
prices = [50, 30, 20, 40, 60]
print("Original list:", prices)

# Accessing elements (indexing)
print("First item:", prices[0])      # 50
print("Last item:", prices[-1])      # 60

# Slicing (getting a sublist)
print("First 3 items:", prices[0:3])  # [50, 30, 20]
print("Items from index 2 to end:", prices[2:])  # [20, 40, 60]

#  Modifying elements
prices[1] = 35     # Change second item from 30 to 35
print("After modifying second item:", prices)  # [50, 35, 20, 40, 60]

# append() → Add an item to the end
prices.append(25)
print("After append(25):", prices)   # [50, 35, 20, 40, 60, 25]

#  pop() → Remove and return last item
last_price = prices.pop()
print("Popped item:", last_price)    # 25
print("After pop():", prices)        # [50, 35, 20, 40, 60]

# sort() → Sort the list in ascending order
prices.sort()
print("After sort():", prices)       # [20, 35, 40, 50, 60]

#reverse() → Reverse the list
prices.reverse()
print("After reverse():", prices)    # [60, 50, 40, 35, 20]
