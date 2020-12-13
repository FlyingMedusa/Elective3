import nltk                           
from nltk.book import *   

goodcount = len([j for j in text3 if j.lower() == 'good'])
evilcount = len([j for j in text3 if j.lower() == 'evil'])

print("good =", goodcount,', evil =', evilcount)