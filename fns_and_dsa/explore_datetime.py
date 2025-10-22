from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    # Get the current date and time
    current_date = datetime.now()
    # Format it to a readable string
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return so we can reuse it in other functions


def calculate_future_date():
    """Ask user for days to add and display the future date."""
    try:
        # Ask the user how many days to add
        days = int(input("Enter the number of days to add to the current date: "))
        
        # Get the current date
        current_date = datetime.now()
        
        # Calculate future date
        future_date = current_date + timedelta(days=days)
        
        # Format future date as YYYY-MM-DD
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        
        print(f"Future date: {formatted_future_date}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")


def main():
    """Main function to run both parts."""
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()
