import re
import nltk #if giving error of no module use command 'pip install nltk'
from nltk.corpus import stopwords
import wordcloud as wc
import matplotlib.pyplot as plt #if giving error of no module use command 'pip install matplotlib.pyplot'

#before running should use these two commands
#'nltk.download_gui()' while running python, download package stopwords
#'conda install -c conda-forge wordcloud=1.2.1' in the Anaconda Prompt


data = {}

data['gibberish'] = open('/Users/TCR/Documents/sd_pyds_a02/data.txt','r',encoding='utf-8').read()

print(data['gibberish'][:1000])

for k in data.keys():
	data[k] = data[k].lower()
	
print(data['gibberish'][:1000])

for k in data.keys():
	data[k] = re.sub(r'[-./?!,":;()\']',' ', data[k])
	
print(data['gibberish'][:1000])

for k in data.keys():
	data[k] = re.sub('[-[0-9]',' ', data[k])
	
print(data['gibberish'][:1000])

stopwords_list = stopwords.words('english')

for k in data.keys():
	data[k] = data[k].split()
	
for k in data.keys():
	data[k] = [w for w in data[k] if not w in stopwords_list]
	
print(data['gibberish'][:1000])

wordcloud = wc.WordCloud(width=300,height = 300).generate(' '.join(data['gibberish']))
plt.figure(figsize=(20,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()