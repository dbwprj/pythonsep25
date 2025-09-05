import timeit

class Machine:
    def __init__(self, name, status, production_rate):
        self.name = name
        self.status = status
        self.production_rate = production_rate

    def __repr__(self):
        return f"Machine(name={self.name}, status={self.status}, production_rate={self.production_rate})"

# List of machines with integer keys (machine id) and values as Machine objects
machines = {
    101: Machine("Machine A", "Operational", 120.5),
    102: Machine("Machine B", "Under Maintenance", 95.0),
    103: Machine("Machine C", "Operational", 150.3),
    104: Machine("Machine D", "Operational", 110.0),
    105: Machine("Machine E", "Under Maintenance", 80.2)
}

# Convert the dictionary into a list of tuples (key, value) so we can filter by different criteria
machine_list = list(machines.items())

# --- 1. Using List Comprehension to filter machines with production rate > 100 ---
def filter_with_list_comprehension():
    return [machine for key, machine in machine_list if machine.production_rate > 100]

# --- 2. Using filter() function to filter machines with production rate > 100 ---
def filter_with_filter_function():
    return list(filter(lambda x: x[1].production_rate > 100, machine_list))

# --- Measure Time Taken for Both Approaches Using timeit ---

# Time the list comprehension function
list_comprehension_time = timeit.timeit(filter_with_list_comprehension, number=10)

# Time the filter function
filter_function_time = timeit.timeit(filter_with_filter_function, number=10)

# --- Print the results ---
print(f"Time taken by List Comprehension (10 executions): {list_comprehension_time:.6f} seconds")
print(f"Time taken by filter() function (10 executions): {filter_function_time:.6f} seconds")
