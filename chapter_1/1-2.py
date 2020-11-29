def is_even(k: int):
    even_on = False
    for i in range(0, k):
        even_on = not even_on
    return not even_on

print(is_even(5)) # False
print(is_even(4)) # True
