def sum_of_odd_squares(n: int):
    if n < 0:
        raise ValueError('Number must be non-negative')
    soos = 0
    for i in range(0, n):
        if i % 2 != 0:
            soos += i ** 2
    return soos

print(sum_of_odd_squares(5)) # 10
