# Writing to the file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text.\n")
    file.write("Writing to files in Python is easy!\n")

# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)

'''
open("example.txt", "w")
This opens a file named "example.txt".
The "w" means write mode — you want to write data to this file.
If the file doesn’t exist, Python creates it.

If the file exists, opening in "w" mode erases the previous content (overwrites).

with keyword
This creates a context manager.
It automatically handles opening and closing the file.
Even if there’s an error while working with the file,
the file will be properly closed when the block ends.
This is safer and cleaner than manually opening and closing files.

as file
Assigns the opened file object to the variable file.
You use this variable to read from or write to the file.

'''
