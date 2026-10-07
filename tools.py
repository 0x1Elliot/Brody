import re

# This module provides utility functions for calculating relative dates and times, getting the current date and time, evaluating mathematical expressions, and parsing user messages for relative date and time requests. It uses the `datetime` module to perform date and time calculations and formatting.
from datetime import datetime, timedelta


def calculate_relative_datetime(years=0, days=0, hours=0, minutes=0):
    now = datetime.now()

    try:
        target_datetime = now.replace(year=now.year + years)
    except ValueError:
        target_datetime = now.replace(
            year=now.year + years,
            month=2,
            day=28
        )

    target_datetime = target_datetime + timedelta(
        days=days,
        hours=hours,
        minutes=minutes
    )

    return target_datetime.strftime("%A, %B %d, %Y at %I:%M %p")


def get_current_datetime():
    now = datetime.now()

    return now.strftime("%A, %B %d, %Y %I:%M %p")


# This 'calculate' function takes a mathematical expression as input and evaluates it. It first checks if the expression contains only allowed characters (digits, operators, parentheses, and spaces). If any invalid characters are found, it returns an error message. If the expression is valid, it attempts to evaluate it using the `eval` function and returns the result as a string. If the evaluation fails for any reason, it returns an error message indicating that the calculation failed.
def calculate(expression):
    allowed_characters = "0123456789+-*/(). "

    for character in expression:
        if character not in allowed_characters:
            return "Invalid calculation."

    try:
        return str(eval(expression))
    except Exception:
        return "Calculation failed. Please check your expression and try again."


# The 'parse_relative_datetime' function takes a user message as input and checks for specific keywords that indicate a request for a relative date and time. It looks for terms like "tomorrow", "yesterday", "last year", and "next year". Based on the detected keyword, it returns a dictionary containing the number of days, hours, and minutes to adjust from the current date and time. If no relevant keywords are found, it returns a dictionary with zero adjustments.
def parse_relative_datetime(message):
    text = message.lower()

    if "tomorrow" in text:
        return {
        "years": 0,
        "days": 1,
        "hours": 0,
        "minutes": 0
        }

    if "yesterday" in text:
        return {
        "years": 0,
        "days": -1,
        "hours": 0,
        "minutes": 0
        }

    if "last year" in text:
        return {
        "years": -1,
        "days": 0,
        "hours": 0,
        "minutes": 0
    }

    if "next year" in text:
        return {
        "years": 1,
        "days": 0,
        "hours": 0,
        "minutes": 0
    }

    day_match = re.search(r"(\d+)\s+days?", text)
    hour_match = re.search(r"(\d+)\s+hours?", text)
    minute_match = re.search(r"(\d+)\s+minutes?", text)

    days = int(day_match.group(1)) if day_match else 0
    hours = int(hour_match.group(1)) if hour_match else 0
    minutes = int(minute_match.group(1)) if minute_match else 0

    if "ago" in text:
        days *= -1
        hours *= -1
        minutes *= -1

    return {
        "years": 0,
        "days": days,
        "hours": hours,
        "minutes": minutes
    }