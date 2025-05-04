import datetime

def date_difference(date: str, date1: str) -> int:
    """
    Calculates the absolute number of days between two dates.

    Parameters:
    - date (str): The first date in 'YYYY-MM-DD' format.
    - date1 (str): The second date in 'YYYY-MM-DD' format.

    Returns:
    - int: Absolute difference in days between the two dates.
    """
    try:
        d1 = datetime.datetime.strptime(date, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        return abs((d2 - d1).days)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")

# Example usage
print(date_difference("2025-03-01", "2025-05-12"))