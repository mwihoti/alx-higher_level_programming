#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    nm1, nm2 = len(tuple_a), len(tuple_b)
    new_tuple = (
            (tuple_a[0] if nm1 >= 1 else 0) + (tuple_b[0] if nm2 >= 1 else 0),
            (tuple_a[1] if nm1 >= 2 else 0) + (tuple_b[1] if nm2 >= 2 else 0))
    return new_tuple
