import json
import os

FILE_NAME = "portfolio.json"

# Ensure file exists
def _init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)

def read_portfolio():
    _init_file()
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def write_portfolio(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_stock(ticker, quantity, price):
    portfolio = read_portfolio()
    for stock in portfolio:
        if stock["ticker"] == ticker:
            return False, "Stock already exists."
    portfolio.append({
        "ticker": ticker,
        "quantity": quantity,
        "price": price
    })
    write_portfolio(portfolio)
    return True, "Stock added."

def update_stock(ticker, quantity=None, price=None):
    portfolio = read_portfolio()
    for stock in portfolio:
        if stock["ticker"] == ticker:
            if quantity is not None:
                stock["quantity"] = quantity
            if price is not None:
                stock["price"] = price
            write_portfolio(portfolio)
            return True, "Stock updated."
    return False, "Stock not found."

def delete_stock(ticker):
    portfolio = read_portfolio()
    new_portfolio = [s for s in portfolio if s["ticker"] != ticker]
    if len(new_portfolio) == len(portfolio):
        return False, "Stock not found."
    write_portfolio(new_portfolio)
    return True, "Stock deleted."

def get_all_stocks():
    return read_portfolio()
