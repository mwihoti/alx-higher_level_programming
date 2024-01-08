#!/usr/bin/env python3
def no_c(my_string):
    new_str = [char for char in my_string if char.lower() != 'c']
    return "".join(new_str)
