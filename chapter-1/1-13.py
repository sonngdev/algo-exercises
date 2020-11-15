def my_reverse(data):
    l = []
    for i in data:
        l.insert(0, i)
    return l

print(my_reverse([1, 2, 3, 4])) # [4, 3, 2, 1]
