import re

def isPalind(x):
    x = x.upper()
    x = "".join(re.split("[^A-Z]*", x))
    if(x[::-1]==x):
        return True
    else:
        return False

print(isPalind("Go hang a salami - I'm a lasagna hog."))
        
