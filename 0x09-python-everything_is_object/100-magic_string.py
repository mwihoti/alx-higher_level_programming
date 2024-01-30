#!/usr/bin/python3
def magic_string(my_list=[0]):
    my_list[0] = my_list[0] + 1
    return "BestSchool"+(", BestSchool"*(my_list[0] - 1))
