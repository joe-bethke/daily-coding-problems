
def is_palindrome(s):
    return s == "".join(reversed(s))


def solve(words):
    return [(i, j)
            for i, wi in enumerate(words)
            for j, wj in enumerate(words)
            if i != j and is_palindrome(wi + wj)]

print(solve(['code', 'edoc', 'da', 'd']))