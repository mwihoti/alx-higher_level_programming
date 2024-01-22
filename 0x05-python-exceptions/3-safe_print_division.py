#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divs = a / b
    except (ZeroDivisionError, FloatingPointError):
        divs = None
    finally:
        print("Inside result: {}".format(divs))
    return divs
