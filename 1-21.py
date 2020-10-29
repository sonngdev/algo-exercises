inputs = []

try:
    while True:
        el = input('Type something, or press Ctrl-D to exit: ')
        inputs.append(el)
except EOFError as e:
    print(list(reversed(inputs)))
