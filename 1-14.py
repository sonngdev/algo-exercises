def has_odd_product(data):
    for i in data:
        for k in data[i:]:
            if (i * k) % 2 != 0:
                return True
    return False

print(has_odd_product([1, 2, 4])) # False
print(has_odd_product([1, 2, 3])) # True
