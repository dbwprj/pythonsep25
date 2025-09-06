import json

# Sample data to write to JSON
data = {
    "name": "Ramesh",
    "age": 30,
    "is_investor": True,
    "portfolio": ["HDFC", "SUN", "AIR"]
}

# Writing data to JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data has been written to data.json")

# Reading data from JSON file
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("Data read from data.json:")
print(loaded_data)
