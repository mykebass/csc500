def get_positive_integer(prompt):
    """Prompt the user until a valid positive integer is entered."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive integer.")

def calculate_points(num_books):
    """Calculate points based on the number of books."""
    points = 0
    if 2 <= num_books < 4:
        points = 5
    elif 4 <= num_books < 6:
        points = 15
    elif 6 <= num_books < 8:
        points = 30
    elif num_books >= 8:
        points = 60
    return points

def main():
    # Ask for number of books
    num_books = get_positive_integer("Enter the number of books: ")
    
    # Calculate points
    num_points = calculate_points(num_books)
    
    # Display results
    print(f"\nTotal number of books: {num_books}")
    print(f"Total points awarded: {num_points}")

if __name__ == "__main__":
    main()