def fits_formula(a: int, b: int, c: int):
    x, y, z = sorted([a, b, c]) # x <= y <= z
    return x + y == z or x * y == z

print(fits_formula(6, 2, 3)) # True
print(fits_formula(6, 2, 4)) # True
print(fits_formula(6, 2, 1)) # False
