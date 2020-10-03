import pickle

def save_dict(dict1,filePath):
    with open(filePath, 'wb') as file:
        pickle.dump(dict1, file)

def load_dict(filePath):
    with open(filePath, 'rb') as file:
        return pickle.load(file)


dict1={
    "a":1,"b":2,"c":3
    }
save_dict(dict1,'testDict.pickle')

print(load_dict('testDict.pickle'))
