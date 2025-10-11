# match_case_calculator.py

# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user for operation
operation = input("Choose the operation (+, -, *, /): ")

# Match Case statement to handle operations
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation.")
