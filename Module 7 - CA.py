# Dictionaries containing course information
# Each dictionary maps course numbers to their respective details

# Dictionary for room numbers
room_numbers = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

# Dictionary for instructors
instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

# Dictionary for meeting times
meeting_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# Display course information
def display_course_info(course_number):
    # Retrieve the room number, instructor, and meeting time for the inputted course number
    room_number = room_numbers.get(course_number)
    instructor = instructors.get(course_number)
    meeting_time = meeting_times.get(course_number)
    
    # Check if all information is available for the inputted course number
    if room_number and instructor and meeting_time:
        # Print course details if found
        print(f"Course Number: {course_number}")
        print(f"Room Number: {room_number}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
    else:
        # Return False if no information is found
        return False
    # Return True if information is found and displayed
    return True

# Main Program
def main():
    while True:
        # Prompt the user to enter a course number
        course_number = input("Enter a course number (e.g., CSC101): ").strip().upper()
        # Display the course information
        if not display_course_info(course_number):
            print(f"No information found for course number: {course_number}")
            try_again = input("Would you like to try again? (yes/no): ").strip().lower()
            if try_again != 'yes':
                print("Goodbye!")
                break
        else:
            break

# Run the program
if __name__ == "__main__":
    main()
