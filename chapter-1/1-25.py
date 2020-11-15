import re

def remove_punctuations(string: str):
    return ''.join(c for c in string if re.match(r"\w|\s", c))

print(remove_punctuations("Let's go. Now")) # Lets go Now
