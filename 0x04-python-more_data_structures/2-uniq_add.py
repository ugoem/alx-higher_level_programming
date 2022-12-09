#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_set = set(my_list)
    for num in my_set:
        sum += num
    return sum
