#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp = []
    for i in range(len(my_list)):
        cp.append(my_list[i])
    if idx < 0 or idx >= len(my_list):
        return cp
    else:
        cp = cp[:idx] + [element] + cp[idx + 1:]
        return cp
