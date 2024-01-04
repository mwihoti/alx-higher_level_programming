#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:

        k = add(a, b)
        for i in range(4, 6):
            k = add(k, i)
        return k
    else:
        return sub(a, b)
