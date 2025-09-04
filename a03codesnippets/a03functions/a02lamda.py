

# Define operations using lambda, Ramesh wrote it
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b

# Main function ,Suresh is writing this.
def calculator():
    print("Welcome to the Lambda Calculator!")
    print("Choose an operation: +, -, *")

    operation = input("Enter operation (+, -, *): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Dictionary to map symbols to lambda functions
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply
    }

    # Check and perform operation
    if operation in operations:
        result = operations[operation](num1, num2) #observe how functions are going to called.
        print(f"The result is: {result}")
    else:
        print("Invalid operation.")

# Call the calculator
calculator()
