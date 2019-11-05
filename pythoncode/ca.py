import csv
outputFile = open('output1.csv','w',newline = '')
outputWriter = csv.writer(outputFile)

outputWriter.writerow(['123','lack','2000'])
outputWriter.writerow(['11','hack','2001'])
outputWriter.writerow(['12','kack','2002'])
outputWriter.writerow(['13','jack','20056'])
outputWriter.writerow(['124','mack','200141'])
outputFile.close()
print('Done....')
