def prefix_suffix_sum(arr: list[int]) -> int:
    arr_sum = 0
    for num in arr:
        arr_sum += num

    prev_sum = 0
    largest_sum = None
    for i in range(len(arr)):
        prefix_sum = prev_sum + arr[i]
        suffix_sum = arr_sum - prev_sum
        if prefix_sum == suffix_sum and (largest_sum is None or largest_sum < prefix_sum):
            largest_sum = prefix_sum
        prev_sum = prefix_sum

    return largest_sum


# arr[0..3] == arr[3..6]
assert prefix_suffix_sum([-1, 2, 3, 0, 3, 2, -1]) == 4
# arr[0..3] == arr[3..7]
assert prefix_suffix_sum([-2, 5, 3, 1, 2, 6, -4, 2]) == 7
