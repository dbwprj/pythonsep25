class Stock:
    def __init__(self, ticker, price, quantity):
        self.ticker = ticker
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        """Update the stock's current price."""
        self.price = new_price

    def total_value(self):
        """Calculate the total value of the stock holding."""
        return self.price * self.quantity

    def display_info(self):
        """observe how multiline grouping is taking place by using ()"""
        info = (
            f"Stock: {self.ticker}\n"
            f"Price per share: ${self.price:.2f}\n"
            f"Quantity: {self.quantity} shares\n"
            f"Total value: ${self.total_value():.2f}\n"
            + "-" * 30
        )
        return info



# Create stock objects
apple = Stock("AAPL", 150.25, 10)
tesla = Stock("TSLA", 700.50, 5)

# Print returned string
print(apple.display_info())
print(tesla.display_info())

# Update and print again
apple.update_price(155.75)
print("After price update:")
print(apple.display_info())
