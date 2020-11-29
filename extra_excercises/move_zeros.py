from typing import Iterable

def move_zeros(arr: Iterable[int]):
    zero_index = None
    number_index = 0

    while number_index <= len(arr) - 1:
        if arr[number_index] == 0 and zero_index is None:
            zero_index = number_index
        elif arr[number_index] == 0 and zero_index is not None:
            pass
        elif arr[number_index] != 0 and zero_index is None:
            pass
        elif arr[number_index] != 0 and zero_index is not None:
            arr[zero_index], arr[number_index] = arr[number_index], arr[zero_index]
            zero_index += 1

        number_index += 1

arr1 = [1, 0, 0, 0, 9, 7, 0 ,5]
move_zeros(arr1)
assert(arr1 == [1, 9, 7, 5, 0, 0, 0, 0])

arr2 = [0, 0, 0, 0, 0, 0, 0, 1]
move_zeros(arr2)
assert(arr2 == [1, 0, 0, 0, 0, 0, 0, 0])

arr3 = [0, 1, 0, 2, 0, 3, 0, 4]
move_zeros(arr3)
assert(arr3 == [1, 2, 3, 4, 0, 0, 0, 0])

arr4 = [1, 0, 2, 0, 3, 0, 4, 0]
move_zeros(arr4)
assert(arr4 == [1, 2, 3, 4, 0, 0, 0, 0])
