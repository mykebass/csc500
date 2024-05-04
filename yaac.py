def yet_another_alarm_clock():
    print("Welcome to Yet Another Alarm Clock (YAAC)!")
    
    while True:
        try:
            current_time = int(input("Enter the current time (0-23 hours): "))
            if not 0 <= current_time <= 23:
                print("The time must be between 0 and 23.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value between 0 and 23.")
    
    while True:
        try:
            hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
            if hours_to_wait < 0:
                print("Please enter a positive number of hours.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive numerical value for hours.")

    # Calculate the time when the alarm will go off
    alarm_time = (current_time + hours_to_wait) % 24
    
    # Display the result
    print(f"The alarm will go off at {alarm_time}:00 on a 24-hour clock.")

if __name__ == "__main__":
    yet_another_alarm_clock()