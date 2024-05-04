# Tipsy: A Tip Calculator Program

def calculate_total_meal_cost():
    while True:
        try:
            # Ask the user for the charge for food, ensuring input is a number
            food_charge = float(input("Enter the charge for your meal: "))
            if food_charge < 0:
                print("Please enter a positive number.")
                continue
            break  # Exit loop if input is valid
        except ValueError:
            print("Please enter a numerical value.")
    
    # Constants for the tip and tax percentages
    TIP_PERCENTAGE = 18 / 100
    TAX_PERCENTAGE = 7 / 100
    
    # Calculate the tip and tax amounts
    tip_amount = food_charge * TIP_PERCENTAGE
    tax_amount = food_charge * TAX_PERCENTAGE
    
    # Calculate total amount
    total_amount = food_charge + tip_amount + tax_amount
    
    # Display the results
    print("\nBill Details:")
    print(f"Food Charge: ${food_charge:.2f}")
    print(f"Tip (18%): ${tip_amount:.2f}")
    print(f"Sales Tax (7%): ${tax_amount:.2f}")
    print("---------------------------")
    print(f"Total Amount Due: ${total_amount:.2f}")

if __name__ == "__main__":
    calculate_total_meal_cost()