from random import randrange

def my_choice(data):
    maximum = max(data)
    minimum = min(data)

    i = randrange(minimum, maximum + 1)
    while (i not in data):
        i = randrange(minimum, maximum + 1)
    return i

print(my_choice([5, 90, 25, 50]))
