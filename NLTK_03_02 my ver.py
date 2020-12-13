import nltk                           
from nltk.book import *   
import matplotlib.pyplot as plt

fdist = FreqDist(x.lower() for x in text2)
comm_50 = fdist.most_common(50)
#fdist.plot(50,title='Frequency distribution for 50 most common tokens in our text collection')

x_axis = [el[0] for el in comm_50]
y_axis = [el[1] for el in comm_50]

plt.figure(figsize=(16,3)) 
plt.bar(x_axis, y_axis, color = 'pink')
plt.xticks(x_axis, rotation='vertical')
plt.title("50 most frequent types and their number of occurrences")
plt.show()

print("50 most frequent types are responsible for", sum(y_axis),"token occurrences, which constitutes", str(round((sum(y_axis)/len(text2))*100,2)) + "% of all",len(text2),"tokens.")