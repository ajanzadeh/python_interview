# how many times each word in a file has been repated

from collections import defaultdict

def repeate(path):
    dic = {}
    sort_dic = {}
    with open(path,"r") as f:
        lines = f.read().splitlines()

    for lin in range(0,len(lines)):
        words = lines[lin].split()
        for word in range(0,len(words)):
            if words[word] in dic:
                dic[words[word]] +=1
            else:
                dic.setdefault(words[word],0)
        sort_dic = {k: v for k, v in sorted(dic.items(), reverse=True, key=lambda x: x[1])}
    print(sort_dic)
repeate("algorithms/word_frequencies_text.txt")
