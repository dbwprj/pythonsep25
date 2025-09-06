def calculate_roi():
    try:
        initial = float(input("Enter initial investment amount: "))
        final = float(input("Enter final value of investment: "))

        roi = ((final - initial) / initial) * 100
        print(f"Return on Investment (ROI): {roi:.2f}%")

    except ValueError:
        print("Error: Please enter valid numeric input.")
    except ZeroDivisionError:
        print("Error: Initial investment cannot be zero.")
    finally:
        print("Thank you for using the ROI calculator.")

# Run the function
calculate_roi()
