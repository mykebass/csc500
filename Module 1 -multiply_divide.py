# Ask the user to input the first number
num1 = float(input("Enter the first number (num1): "))

# Ask the user to input the second number
num2 = float(input("Enter the second number (num2): "))

# Function to format the result (remove decimals if whole number)
def format_result(result):
    return int(result) if result.is_integer() else result

# Calculate the multiplication of num1 and num2
multiplication_result = num1 * num2

# Check for division by zero before dividing
if num2 == 0:
    division_result = "undefined (cannot divide by zero)"
else:
    # Calculate the division of num1 by num2
    division_result = num1 / num2
    # Format the division result if not undefined
    division_result = format_result(division_result)

# Display the results with formatting
print(f"The multiplication of {num1} and {num2} is: {format_result(multiplication_result)}")
if division_result == "undefined (cannot divide by zero)":
    print("The division of num1 by num2 is undefined (cannot divide by zero).")
else:
    print(f"The division of {num1} by {num2} is: {division_result}")