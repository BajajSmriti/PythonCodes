import re
from collections import Counter

def load_file(filePath):
    with open(filePath, 'r+') as file:
        all_words = re.findall(r"[0-9a-zA-z-']+",file.read())
        all_words = [word.upper() for word in all_words]
        print("Total words: ",len(all_words))

        words_counts = Counter()
        for word in all_words:
            words_counts[word] +=1

        print("Top 20 words: ")
        for word in words_counts.most_common(20):
            print(word[0], '\t', word[1])

load_file("input.txt")
