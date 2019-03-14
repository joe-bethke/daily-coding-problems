"""
This problem was asked by Palantir.
Write an algorithm to justify text.
Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.
For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""


def solve(words, line_length):
    # Needs logic for if a single word is longer than the line length
    lines = list()
    line = list()
    for word in words:
        word = f" {word}" if line else word
        if sum(map(len, line)) + len(word) <= line_length:
            line.append(word)
        else:
            lines.append(line)
            line = [word[1:]]
    if line and line not in lines:
        lines.append(line)
    for line in lines:
        word_index = 0
        while sum(map(len, line)) < line_length:
            if word_index == len(line):
                word_index = 0
            if len(line) == 1 or word_index != len(line) - 1:
                # append a space to the word if it's the only word on the line, or is not the last word on the line
                line[word_index] += " "
            word_index += 1
    justified_words = ["".join(line) for line in lines]
    return justified_words

solutions = [
    solve(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16),
    solve(["haiku", "nothisisnotactuallyahaiku", "h", "a", "i", "k", "u", "    "], 5),
    solve(["hello", "this", "is", "my", "twenty-eigth", "daily", "coding", "problem"], 14),\
]

for solution in solutions:
    print("|\n".join(solution) + "|\n")
