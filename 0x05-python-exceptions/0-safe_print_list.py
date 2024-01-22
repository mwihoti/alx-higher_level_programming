#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    x_elem = 0
    for i in range(int(x)):
        try:
            print("{}".format(my_list[i]), end="")
            x_elem += 1
        except IndexError:
            pass
    print()
    return x_elem
