
def solve(doc, write_doc=dict(), higher_key=""):
    for key, value in doc.items():
        new_key = ".".join((higher_key, key)) if higher_key else key
        if isinstance(value, dict):
            solve(value, write_doc=write_doc, higher_key=new_key)
        else:
            write_doc[new_key] = value
    return write_doc


new = solve({
    "a": 1,
    "b": 2,
    "c": {
        "d": 3,
        "e": 4
    },
    "f": 5,
    "g": {
        "h": 6,
        "i": 7,
        "j": {
            "k": 8,
        }
    }
})
print(new)