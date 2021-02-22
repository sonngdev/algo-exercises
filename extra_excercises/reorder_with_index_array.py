def reorder_with_index_array(arr: list[int], index: list[int]) -> None:
    """
    This function will perform at most N - 1 swaps, so time complexity is O(n)
    """
    for i in range(len(index)):
        while index[i] != i:
            val = index[i]
            index[i], index[val] = index[val], index[i]
            arr[i], arr[val] = arr[val], arr[i]


arr1 = [10, 11, 12]
index1 = [1, 0, 2]
reorder_with_index_array(arr1, index1)
assert arr1 == [11, 10, 12]
assert index1 == [0, 1, 2]

arr2 = [50, 40, 70, 60, 90]
index2 = [3, 0, 4, 1, 2]
reorder_with_index_array(arr2, index2)
assert arr2 == [40, 60, 90, 50, 70]
assert index2 == [0, 1, 2, 3, 4]

arr3 = [11, 12, 13, 14, 15, 16]
index3 = [5, 2, 3, 0, 1, 4]
reorder_with_index_array(arr3, index3)
assert arr3 == [14, 15, 12, 13, 16, 11]
assert index3 == [0, 1, 2, 3, 4, 5]
