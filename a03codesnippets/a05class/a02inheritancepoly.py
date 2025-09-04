# Base class
class FinancialInstrument:
    def __init__(self, name):
        self.name = name

    def get_value(self):
        """Calculate the value of the instrument (to be overridden)."""
        return 0

    def display_info(self):
        """Returns a generic summary of the instrument."""
        return f"Instrument: {self.name}, Value: ${self.get_value():.2f}"


# Derived class 1: Stock
class Stock(FinancialInstrument):
    def __init__(self, name, price_per_share, quantity):
        super().__init__(name)
        self.price_per_share = price_per_share
        self.quantity = quantity

    def get_value(self):
        return self.price_per_share * self.quantity


# Derived class 2: Bond
class Bond(FinancialInstrument):
    def __init__(self, name, face_value, interest_rate, years):
        super().__init__(name)
        self.face_value = face_value
        self.interest_rate = interest_rate
        self.years = years

    def get_value(self):
        # Simple interest calculation: FV + (FV * r * t)
        return self.face_value + (self.face_value * self.interest_rate * self.years)


# --- Polymorphism in action ---

# Create a list of different financial instruments
portfolio = [
    Stock("AAPL", 150.0, 10),
    Bond("US Treasury", 1000, 0.05, 5),
    Stock("TSLA", 700.0, 3)
]

# Display value of each using polymorphic method
for instrument in portfolio:
    print(instrument.display_info())
