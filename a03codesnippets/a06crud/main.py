from portfolio import add_stock, update_stock, delete_stock, get_all_stocks

def print_menu():
    print("\n--- Portfolio Manager ---")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Update Stock")
    print("4. Delete Stock")
    print("5. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            ticker = input("Enter stock ticker: ").upper()
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per share: "))
            success, message = add_stock(ticker, quantity, price)
            print(message)

        elif choice == "2":
            stocks = get_all_stocks()
            if not stocks:
                print("Portfolio is empty.")
            else:
                print("\nYour Portfolio:")
                for s in stocks:
                    print(f"{s['ticker']} - {s['quantity']} shares at ${s['price']:.2f} each")

        elif choice == "3":
            ticker = input("Enter stock ticker to update: ").upper()
            quantity = input("Enter new quantity (or press Enter to skip): ")
            price = input("Enter new price (or press Enter to skip): ")

            quantity = int(quantity) if quantity else None
            price = float(price) if price else None

            success, message = update_stock(ticker, quantity, price)
            print(message)

        elif choice == "4":
            ticker = input("Enter stock ticker to delete: ").upper()
            success, message = delete_stock(ticker)
            print(message)

        elif choice == "5":
            print("Exiting portfolio manager.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
