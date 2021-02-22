def uniq_c_unix(arr: list[str]) -> list[list]:
    if len(arr) == 0:
        return []

    result = []

    current = None
    repeated = 0
    for char in arr:
        if char == current:
            repeated += 1
            continue

        if current is not None:
            result.append([current, repeated])
        current = char
        repeated = 1

    result.append([current, repeated])
    return result


assert uniq_c_unix(['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c']) == [
    ['a', 2], ['b', 2], ['c', 1], ['a', 1], ['b', 1], ['c', 1]
]
assert uniq_c_unix(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']) == [['a', 8]]
