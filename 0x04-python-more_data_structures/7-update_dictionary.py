#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    up_dic = {key: value}
    a_dictionary.update(up_dic)
    return a_dictionary
