# observe funtions do logic and dont do ui.
#only one function deals with ui , we can move this into separate files later on.


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select operation: +, -, *")

    operation = input("Enter operation (+, -, *): ")

    # Take two numbers as input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the operation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    else:
        print("Invalid operation selected.")
        return

    # Print the result
    print(f"The result is: {result}")

# Call the calculator function
calculator()



def calculate_rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter



a, p = calculate_rectangle(10, 5) # returning a tuple and unpacked.
print("Area:", a)        
print("Perimeter:", p)  