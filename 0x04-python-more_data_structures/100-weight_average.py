#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avg = 0
    dv = 0
    for m in my_list:
        avg += m[0] * m[1]
        dv += m[1]
    return float(avg / dv)
