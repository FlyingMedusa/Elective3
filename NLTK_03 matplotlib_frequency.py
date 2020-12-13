import nltk                           
from nltk.book import *   
import matplotlib.pyplot as plt

fd = FreqDist(x.lower() for x in text2)   #we consider all tokens: alphabetic, punctuation and numeric
fd.plot(50, cumulative=True)

cumul = 0
length = len(text2)
i = 1
print('{0:>6}{1:>10}{2:>10}{3:>10}{4:>10}'.format('no', 'type', 'raw fq', 'cumul fq', 'perc'))
for tok in fd.most_common(50):
    cumul+=tok[1]
    perc = round(cumul/length*100, 2)
    print('{0:6}{1:>10}{2:10}{3:10}{4:10}'.format(i, tok[0], tok[1], cumul, perc))         #optional
    i += 1
print('\n50 most freq types are responsible for',cumul,'token occurrences, which constitutes',perc,'% of all',length,'tokens. 50% of',length,'would be',length/2)