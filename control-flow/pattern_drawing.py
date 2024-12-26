#!/usr/bin/env python3

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the size is positive
if size > 0:
    row = 0
    # Use a while loop to handle rows
    while row < size:
        # Use a for loop to handle columns
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1
else:
    print("Please enter a positive integer.")

