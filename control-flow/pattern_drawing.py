# pattern_drawing.py
# This program prints a square pattern of asterisks using nested loops

# Ask the user for pattern size and convert to integer
size = int(input("Enter the size of the pattern: "))

# Initialize a variable to keep track of rows
row = 0

# Outer loop - while loop for rows
while row < size:
    # Inner loop - for loop for columns
    for col in range(size):
        print("*", end="")  # print * without going to new line
    print()  # move to next line after finishing one row
    row += 1  # increment row
