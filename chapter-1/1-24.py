def count_vowels(string: str):
    chars = ['a', 'e', 'i', 'o', 'u']
    vowels = (c for c in string if c in chars)
    return sum(1 for _ in vowels)

print(count_vowels('hello world')) # 3
print(count_vowels('foo bar baz')) # 4
