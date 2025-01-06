from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date(days):
    """
    Calculates the future date by adding a given number of days to the current date.
    :param days: Number of days to add (integer)
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    # Part 1: Display Current Date and Time
    display_current_datetime()

    # Part 2: Calculate Future Date
    try:
        days = int(input("Enter the num

