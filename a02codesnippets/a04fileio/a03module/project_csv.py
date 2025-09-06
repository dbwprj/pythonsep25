import csv

def write_row_to_csv(filename, row):
    """Append a single row (list) to the CSV file.
    Returns True on success, False on failure."""
    try:
        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
        return True
    except Exception as e:
        # You could log the error e if needed
        return False

def read_csv(filename):
    """Read all rows from the CSV file.
    Returns (True, rows) on success, (False, []) on failure."""
    rows = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        return True, rows
    except FileNotFoundError:
        return False, []
    except Exception:
        return False, []
    

#FILENAME = "data.csv"

def menu1():
    while True:
        print("\n--- CSV File Menu ---")
        print("1. Add a row to CSV")
        print("2. Read CSV file")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            row_input = input("Enter comma separated values for the row: ")
            row = [item.strip() for item in row_input.split(",")]
            success = write_row_to_csv(FILENAME, row)
            if success:
                print("Row added successfully.")
            else:
                print("Failed to add row to the CSV file.")
        elif choice == '2':
            success, rows = read_csv(FILENAME)
            if success:
                if rows:
                    print("\nCSV Contents:")
                    for r in rows:
                        print(r)
                else:
                    print("CSV file is empty.")
            else:
                print("Failed to read the CSV file or file does not exist.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    pass
