def sum_of_squares(n: int):
    if n < 0:
        raise ValueError('Number must be non-negative')
    sos = 0
    for i in range(0, n):
        sos += i ** 2
    return sos

print(sum_of_squares(5)) # 30
