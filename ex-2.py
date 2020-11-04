from typing import Iterable, Tuple
from functools import reduce

def calc(ops):
    s = 0
    for num, op in ops:
        if op == '+':
            s += num
        else:
            s -= num
    return s

def build_str(ops):
    s = ''
    for num, op in ops:
        s += op + str(num)
    return s

def insert_operators(arr):
    ops = [[num, '+'] for num in arr]

    sorted_arr = list(reversed(sorted(arr))) # descending order
    biggest_num_index = 0

    result = calc(ops)
    while result != 0:
        # exit if the end of the list is reached
        if biggest_num_index >= len(sorted_arr) - 1:
            return None

        # find the biggest to 'flip' without 'flipping' the sum
        while result < 2 * sorted_arr[biggest_num_index]:
            # continue searching if possible
            if biggest_num_index < len(sorted_arr) - 1:
                biggest_num_index += 1
            # exit if array is invalid
            else:
                return None

        # flip the operator
        for i in range(0, len(ops)):
            if ops[i][0] == sorted_arr[biggest_num_index]:
                ops[i][1] = '-'

        result = calc(ops)
        biggest_num_index += 1

    return build_str(ops)

print(insert_operators([1, 2, 3, 4]))
print(insert_operators([1, 2, 3, 4, 5]))
print(insert_operators([1, 2, 3, 4, 5, 15]))
