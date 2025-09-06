# basic data type in python
business_name = "Abc hotel"           # str
num_employees = 4                      # int
daily_customers = 120                  # int
coffee_price = 2.75                    # float
daily_revenue = daily_customers * coffee_price  # float
expenses = 250.0                       # float
is_profitable = daily_revenue > expenses  # bool

weekly_sales = [300.0, 280.0, 310.0, 275.0, 350.0, 400.0, 360.0]  # list
opening_hours = ("08:00", "21:00")     # tuple
payment_methods = {"cash", "card", "mobile", "card"}  # set (unique)
employee_salaries = {                  # dict
    "Ramesh": 3000,
    "Babu": 2800,
    "Veeresh": 3100,
    "Rama": 2900
}

print(f"{business_name} makes Rs {daily_revenue} per day.")
print("Is the business profitable?", is_profitable)
print("Payment methods used:", payment_methods)


x=3
print(type(x)) # to know the type of the variable... why...
print(type(x).__name__)  # simplified Output: int

x = 42

# dynamic checking of data type.. we will use this during inheritance... later on..
if isinstance(x, int):
    print("x is an integer")
elif isinstance(x, str):
    print("x is a string")
elif isinstance(x, list):
    print("x is a list")
else:
    print("x is of some other type")




#teach the system that Rectangle is a data type , becuase project needs it
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    #@staticmethod
    def describe(length, breadth):
        return f"A rectangle of length {length} and breadth {breadth}."


#creating the variable of the data type Rectangle
rect = Rectangle(10, 5)

print("Area:", rect.area())                        # Output: Area: 50
print("Perimeter:", rect.perimeter())              # Output: Perimeter: 30
print("Description:", Rectangle.describe(10, 5))   # Output: A rectangle of length 10 and breadth 5.


