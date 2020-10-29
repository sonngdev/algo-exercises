from typing import Iterable

def minmax(data: Iterable):
    minimum = float('inf')
    maximum = float('-inf')
    for i in data:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
    return minimum, maximum

print(minmax([5, 7, 9, 1, 2])) # (1, 9)
