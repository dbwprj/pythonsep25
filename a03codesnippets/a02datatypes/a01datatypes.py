# basic data type in python
business_name = "Abc hotel"           # str
num_employees = 4                      # int
daily_customers = 120                  # int
coffee_price = 2.75                    # float
daily_revenue = daily_customers * coffee_price  # float
expenses = 250.0                       # float
is_profitable = daily_revenue > expenses  # bool

weekly_sales = [300.0, 280.0, 310.0, 275.0, 350.0, 400.0, 360.0]  # list
opening_hours = ("08:00", "18:00")     # tuple
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

