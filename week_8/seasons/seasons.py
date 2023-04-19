from datetime import date
import inflect
import re
import sys

def main():
    birthdate = input("Date of Birth (yyyy-mm-dd): ")
    birthdate = validate(birthdate)
    minutes = calc_minutes(birthdate)

    # convert minutes to text
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    word = words + " minutes"

    print(word.capitalize())



def validate(birthdate : str)-> date:
    """
    Validates a birthdate string in ISO format (YYYY-MM-DD) and returns a date object.

    Args:
        birthdate (str): The birthdate string in ISO format.

    Returns:
        date: The date object representing the validated birthdate.

    Raises:
        SystemExit: If the birthdate string is not in valid ISO format.
    """
    try:
        # Convert the birthdate string to a date object using fromisoformat() method
        birthdate = date.fromisoformat(birthdate)
        return birthdate
    except ValueError:
        # Raise a SystemExit exception with an error message if birthdate is not valid
        sys.exit("Invalid date")


def calc_minutes(birthdate:date) -> int:
    """
    Calculates the number of minutes between the given birthdate and today's date.

    Args:
        birthdate (date): The birthdate as a date object.

    Returns:
        int: The number of minutes between the birthdate and today's date.

    """
    today = date.today()
    diff = today - birthdate
    minutes = diff.days * 24 * 60
    return minutes



if __name__ == "__main__":
    main()