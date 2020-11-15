from typing import Iterable
from re import sub


class TernaryOverflowException(Exception):
    pass


def floor_log(x: int, base: int):
    exp = 0
    while base ** exp < x:
        exp += 1

    return exp if base ** exp == x else exp - 1


def base_10_to_base_3(num: int, num_of_digits: int) -> str:
    nums = [0] * num_of_digits

    while num:
        i = floor_log(num, 3)
        if i < num_of_digits:
            nums[i] += 1
        else:
            raise TernaryOverflowException()
        num -= 3 ** i

    return ''.join(str(num) for num in reversed(nums))


def increment_ternary_number(ops: str) -> str:
    # convert to base 10
    base_10 = int(ops, 3)
    # increment
    base_10 += 1
    # convert back to base 3, return
    base_3 = base_10_to_base_3(base_10, len(ops))
    return base_3


def build_expression(arr: Iterable[int], ops: str) -> str:
    expr = [None] * len(arr) * 2
    op_mappings = {
        '0': '',
        '1': '+',
        '2': '-',
    }


    for i in range(0, len(arr)):
        expr[i * 2] = op_mappings[ops[i]]
        expr[i * 2 + 1] = str(arr[i])

    return ''.join(expr)


def eval_expression(expr: str) -> int:
    expr = sub(r'\b0+(\d+)', r'\1', expr)
    return eval(expr)


def insert_operators(arr):
    num_of_digits = len(arr)
    ops = '0' * num_of_digits

    while True:
        try:
            expr = build_expression(arr, ops)
            if eval_expression(expr) == 0:
                print(expr)
            ops = increment_ternary_number(ops)
        except TernaryOverflowException:
            break


if __name__ == "__main__":
    insert_operators([1, 2, 3, 1, 0, 0, 2, 3])
