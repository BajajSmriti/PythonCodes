
##def sortString(x):
##    dict1={}
##    list1=[]
##    x = x.split()
##    for i in x:
##        dict1[i.upper()]=i
##        list1.append(i.upper())
##        
##    print(dict1)
##    list1.sort()
##    
##    for j in range(len(list1)):
##        list1[j] = dict1[list1[j]]
##        
##    return ' '.join(list1)

def sortString(x):
    words = x.split()
    words = [i.lower() + i for i in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)
print(sortString("banana ORANGE apple Orange orange"))
        
