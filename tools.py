from datetime import datetime


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