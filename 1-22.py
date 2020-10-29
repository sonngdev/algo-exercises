from typing import Iterable

def product_list(a: Iterable[int], b: Iterable[int]):
    return [i * j for i, j in zip(a, b)]

print(product_list([1, 2, 3], [4, 5, 6]))
