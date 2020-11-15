from random import randint

def my_shuffle(data):
    length = len(data)
    ret = [None] * length
    for item in data:
        index = randint(0, length - 1)
        while ret[index]:
            index = randint(0, length - 1)
        ret[index] = item
    return ret

print(my_shuffle([1, 2, 3]))
