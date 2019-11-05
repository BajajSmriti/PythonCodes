import csv

exampleFile = open('output1.csv')
exampleReader = csv.reader(exampleFile)

exampleData = list(exampleReader)

print(exampleData)

for row in exampleData:
    print(str(row))

exampleFile.close()














  
