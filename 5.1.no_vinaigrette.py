"""
Writer: Ranel Ben Simman Tov, 315967703
"""

import datetime as dt
import random
from enum import IntEnum


class Weekday(IntEnum):
    """
    Enum for weekdays
    """
    MONDAY = 0


def get_date(prompt_msg):
    """
    Get a date from the user
    :param prompt_msg:
    :return: date in YYYY-MM-DD format
    """
    try:
        date = input(prompt_msg)
        date = dt.date(*map(int, date.split('-')))  # create date object from input
        return date
    except (ValueError, TypeError):
        print("Incorrect date format, should be YYYY-MM-DD")
        return get_date(prompt_msg)


def generate_random_date(date1, date2):
    """
    Generate a random date between date1 and date2
    :param date1:
    :param date2:
    :return: random date between date1 and date2
    """
    return date1 + (date2 - date1) * random.random()


if __name__ == '__main__':
    # get dates from user
    date1 = get_date("Enter first date in YYYY-MM-DD format: ")
    date2 = get_date("Enter second date in YYYY-MM-DD format: ")

    # generate random date between date1 and date2
    random_date = generate_random_date(date1, date2)
    print(f"The random date between the two dates is {random_date}")

    # check if the random date day is Monday
    if random_date.weekday() == Weekday.MONDAY:
        print("It's Monday! I don't have vinaigrette!")
