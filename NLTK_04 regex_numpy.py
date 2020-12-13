import re
import numpy as np
import matplotlib.pyplot as plt
import nltk

ipa = """nðə nɔ_ːθ wɪnd ən ðə sʌn wə dɪspjutɪŋ wɪt_ʃ wəz ðə strɒŋɡə
wen ə trævlə ke_ɪm əlɒŋ ræpt ɪn ə wɔ_ːm klə_ʊk ðe_ɪ əɡri_ːd ðət ðə wʌn 
hu fɜ_ːst səksidɪd ɪn me_ɪkɪŋ ðə trævlə te_ɪk hɪz klə_ʊk ɒf ʃʊd bi kənsɪdəd strɒŋɡə ðən ði ʌðə
ðen ðə nɔ_ːθ wɪnd blu_ː əz hɑ_ːd əz i kʊd
bət ðə mɔ_ː hi blu_ː ðə mɔ_ː klə_ʊsli dɪd ðə trævlə fə_ʊld hɪz klə_ʊk əra_ʊnd hɪm
ənd ət lɑst ðə nɔ_ːθ wɪnd ɡe_ɪv ʌp ði ətempt
ðen ðə sʌn ʃɒn a_ʊt wɔ_ːmli
ənd əmi_ːdiətli ðə trævlə tʊk ɒf ɪz klə_ʊk
ən sə_ʊ ðə nɔ_ːθ wɪn wəz əbla_ɪd_ʒd tʊ kənfes
ðət ðə sʌn wəz ðə strɒŋɡr əv ðə tu"""
ipal = ipa.split('\n')              #feed each line as separate element of the ipal list
bd = {}                             #initiate dictionary for bigram distributions
for line in ipal:
    line = re.sub(' ','',line)      #remove spaces between words, assume continuous speech within a clause has no pauses "əz hɑ_ːd " -> "əzhɑ_ːd"
    line = re.sub('',' ',line)      #separate symbols by spaces                                            ...-> " ə z h ɑ _ ː d "
    line = line.strip()             #remove leading and trailing spaces created by the above command       ...-> "ə z h ɑ _ ː d"
    line = re.sub('(.) _ (.)','\g<1>_\g<2>',line)  # remove spaces from around _ to make one phoneme       ...-> "ə z h ɑ_ː d"
    fons = line.split(' ')          #...symbol out of three characters; split at spaces into a list        ...-> ['ə', 'z', 'h', 'ɑ_ː', 'd']
    bifo = bigrams(x for x in fons) # create bigrams from the list within a given line
    for big in bifo:                
        if big in bd:
            bd[big] += 1            #feed the bigram into the dic and increment the count if bigram was already there
        else:
            bd[big] = 1
i = 1                               #for printing optional
bl = []                             #barplot or histogram
for b in sorted(bd, key=lambda z: bd[z], reverse=True):
    print('{0:<4}{1:7}{2:2}'.format(i,' '.join(b),bd[b]))
    i+=1
#for the plot
    bl.append(bd[b])
plt.bar(range(len(bl)), bl)   
plt.show()  