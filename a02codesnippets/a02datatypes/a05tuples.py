#  Creating a tuple
product = ("Coffee", 2.99) #read only

#  Accessing tuple elements
print("Product name:", product[0])   # Coffee
print("Product price:", product[1])  # 2.99

#  Tuples can be used in a list
products = [
    ("Coffee", 2.99),
    ("Tea", 1.99),
    ("Juice", 3.49)
]

#  Loop through a list of tuples
for item in products:
    name = item[0]
    price = item[1]
    print(f"{name} - Rs {price}")
