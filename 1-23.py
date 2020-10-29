from typing import Iterable

def guarded_write(data: Iterable, index: int, value):
    try:
        data[index] = value
    except IndexError:
        print('Don’t try buffer overflow attacks in Python!')

data = [1, 2]
guarded_write(data, 0, 5)
print(data)
guarded_write(data, 10, 'hello')
