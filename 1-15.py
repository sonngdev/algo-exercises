def is_distinct(data):
    return data == list(set(data))

print(is_distinct([1, 2, 3])) # True
print(is_distinct([1, 2, 2])) # False
