#!/usr/bin/env python3
def no_c(my_string):
    new_str = list(my_string)
    for str in new_str:
        if str == "c" or str == "C":
            new_str.remove(str)
    return ("".join(new_str))
