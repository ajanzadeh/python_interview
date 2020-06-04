# Word Frequencies: Design a method to find the frequency of occurrences of any given word in a
# a file. What if we were running this algorithm multiple times?
def wf(path,word):
    lines = []
    total = 0
    with open(path, "r") as f:
        lines = f.read().splitlines()
    print(lines)
    for i in range(0,len(lines)):
        if word in lines[i]:
            words = lines[i].split()
            for j in range(0,len(words)):
                if words[j] == word:
                    total +=1
    return total

print(wf("word_frequencies_text.txt","Python"))
