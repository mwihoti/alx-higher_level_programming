#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num1, num2 = len(tuple_a), len(tuple_b)
    new_tuple = ((tuple_a[0] if num1 >= 1 else 0) +
            (tuple_b[0] if num2 >= 1 else 0),
            (tuple_a[1] if num1 >= 2 else 0) +
            (tuple_b[1] if num2 >= 2 else 0))
    return new_tuple
