# Task 1: Perform Basic Mathematical Operations

# Taking two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division with zero check
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Displaying the results
print("\n--- Results ---")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")


output:
Enter the first number: 10
Enter the second number: 5

--- Results ---
Addition: 10.0 + 5.0 = 15.0
Subtraction: 10.0 - 5.0 = 5.0
Multiplication: 10.0 * 5.0 = 50.0
Division: 10.0 / 5.0 = 2.0
