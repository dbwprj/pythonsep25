
# Input: Get income and expenses from the user
income = float(input("Enter your monthly income (Rs): "))
expenses = float(input("Enter your monthly expenses (Rs): "))

savings = income - expenses

# Display result
print("\n--- Financial Summary ---")
print(f"Monthly Income  : Rs{income:.2f}")
print(f"Monthly Expenses: Rs{expenses:.2f}")
print(f"Monthly Savings : Rs{savings:.2f}")

if savings > 0:
    print("Great! You're saving money.")
elif savings == 0:
    print("You're breaking even.")
else:
    print("Warning: You're spending more than you earn.")
