# You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
#
# Note: Each input line ends with a "\n" characte
# nput Format
#
# The first line contains the integer, .
# The next  lines each contain a word.
#
# Output Format
#
# Output  lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
# Sample Input
#
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output
#
# 3
# 2 1 1

from collections import OrderedDict

def run():

    words = {}
    for inputs in range(int(input())):
        word = input()
        words.setdefault(word,0)
        words[word] += 1

    print(len(words))
    repeats = list(words.values())
    print(" ".join(map(str,repeats)))




run()
