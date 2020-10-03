# not secure #import random
import secrets

def gen_pass(count):
    with open('diceware.wordlist.asc.txt','r') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(count)]
    return ' '.join(words)

print(gen_pass(5))
