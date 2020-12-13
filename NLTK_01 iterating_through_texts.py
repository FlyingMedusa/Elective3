import nltk                           
from nltk.book import *   

for i in range(1,10):
    n = 'text' + str(i)
    v = eval(n)
    print(n,len(v))