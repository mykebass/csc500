def get_valid_input(prompt, validation_func, error_message):
    """Prompt the user until a valid input is entered based on validation function."""
    while True:
        try:
            value = validation_func(input(prompt))
            if value <= 0 and validation_func == int:  # Specific check for positive integer inputs
                raise ValueError
            elif value < 0 and validation_func == float:  # Specific check for non-negative float inputs
                raise ValueError
            return value
        except ValueError:
            print(error_message)

def get_positive_integer(prompt):
    """Prompt the user until a valid positive integer is entered."""
    return get_valid_input(prompt, int, "Please enter a valid positive integer.")

def get_non_negative_float(prompt):
    """Prompt the user until a valid non-negative float is entered."""
    return get_valid_input(prompt, float, "Please enter a valid non-negative number.")

def main():
    # Ask for number of years
    num_years = get_positive_integer("Enter the number of years: ")
    
    # Initialize total rainfall
    total_rainfall = 0
    num_months = num_years * 12  # Directly calculating the number of months
    
    # Collect rainfall data
    for year in range(1, num_years + 1):
        print(f"\nYear {year}:")
        for month in range(1, 13):
            rainfall = get_non_negative_float(f"    Enter the rainfall (in inches) for month {month}: ")
            total_rainfall += rainfall
    
    # Calculate and display results
    average_rainfall = total_rainfall / num_months
    print(f"\nTotal number of months: {num_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

if __name__ == "__main__":
    main()