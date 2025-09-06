import math
import random
from datetime import datetime
#From the datetime module, import the datetime class.

# --- math module example ---
number = 16
square_root = math.sqrt(number)
print(f"Square root of {number} is {square_root}")

# --- random module example ---
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# --- datetime module example ---
#datetime.now() is a class method that returns the current date and time
current_time = datetime.now()
print("Current date and time is:", current_time.strftime("%Y-%m-%d %H:%M:%S"))


#look at the import statement

#import datetime
#datetime.datetime.now()