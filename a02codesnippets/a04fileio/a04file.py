import os
import csv

# --- BAD PRACTICES ---

def bad_write_stock_prices():
    print("\n[Bad Write] Writing stock prices without closing file or error handling.")
    file = open("bad_stocks.txt", "w")
    file.write("AAPL,150.25\n")
    file.write("TSLA,700.10\n")
    # Forgot to close the file!
    # file.close()  # Oops!

def bad_read_stock_prices():
    print("\n[Bad Read] Reading stock prices with bare except and no file check.")
    try:
        file = open("bad_stocks.txt", "r")
        data = file.read()
        print("Data read:\n", data)
        file.close()
    except:
        print("An error occurred (but we don't know what!)")

# --- GOOD PRACTICES ---

def good_write_stock_prices():
    print("\n[Good Write] Writing stock prices using 'with' and CSV module.")
    with open("good_stocks.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Ticker", "Price"])
        writer.writerow(["AAPL", 150.25])
        writer.writerow(["TSLA", 700.10])
    print("Successfully wrote to good_stocks.csv")

def good_read_stock_prices():
    print("\n[Good Read] Reading stock prices safely with error handling and 'with'.")
    try:
        with open("good_stocks.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Error: good_stocks.csv file not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# --- Using relative paths for portability ---

def good_write_with_relative_path():
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, "relative_stocks.csv")
    print(f"\n[Good Write with relative path] Writing to {filepath}")

    with open(filepath, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Ticker", "Price"])
        writer.writerow(["MSFT", 300.50])
        writer.writerow(["GOOG", 2800.75])
    print("Successfully wrote to relative_stocks.csv")

def good_read_with_relative_path():
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, "relative_stocks.csv")
    print(f"\n[Good Read with relative path] Reading from {filepath}")

    try:
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Error: relative_stocks.csv file not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# --- Main ---

if __name__ == "__main__":
    # Run bad examples
    bad_write_stock_prices()
    bad_read_stock_prices()

    # Run good examples
    good_write_stock_prices()
    good_read_stock_prices()

    good_write_with_relative_path()
    good_read_with_relative_path()
