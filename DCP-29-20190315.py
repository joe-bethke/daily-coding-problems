"""
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""
import re


def encode(string):
    subs = [sub.group(0) for sub in re.finditer(r"(.)\1*", string)]
    return "".join(f"{len(sub)}{sub[0]}" for sub in subs)


def decode(string):
    counts = [num.group(0) for num in re.finditer(r"(\d)\1*", string)]
    chars = [char.group(0) for char in re.finditer(r"([A-Za-z])\1*", string)]
    return "".join(["".join(char for _ in range(int(num))) for num, char in zip(counts, chars)])

encoded = encode("AAAABBBCCDAA")
print(encoded)
decoded = decode(encoded)
print(decoded)
assert decoded == "AAAABBBCCDAA"