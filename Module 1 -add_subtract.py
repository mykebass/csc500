# Ask the user to input the first number
num1 = float(input("Enter the first number (num1): "))

# Ask the user to input the second number
num2 = float(input("Enter the second number (num2): "))

# Calculate the addition of num1 and num2
addition_result = num1 + num2

# Calculate the subtraction of num1 and num2
subtraction_result = num1 - num2

# Function to format the result (remove decimals if whole number)
def format_result(result):
    return int(result) if result.is_integer() else result

# Display the results with formatting
print(f"The addition of {num1} and {num2} is: {format_result(addition_result)}")
print(f"The subtraction of {num1} from {num2} is: {format_result(subtraction_result)}")