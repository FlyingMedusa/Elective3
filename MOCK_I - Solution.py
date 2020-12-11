esop = [ 'ð ə', 'n ɔː θ', 'w ɪ n d', 'ə n', 'ð ə', 's ʌ n', 'w ə', 'd ɪ s p j u t ɪ ŋ', 'w ɪ tʃ', 'w ə z', 'ð ə', 's t r ɒ ŋ ɡ ə', 'w e n', 'ə', 't r æ v l ə', 'k eɪ m', 'ə l ɒ ŋ', 'r æ p t', 'ɪ n', 'ə', 'w ɔː m', 'k l əʊ k', 'ð eɪ', 'ə ɡ r iː d', 'ð ə t', 'ð ə', 'w ʌ n', 'h u', 'f ɜː s t', 's ə k s i d ɪ d', 'ɪ n', 'm eɪ k ɪ ŋ', 'ð ə', 't r æ v l ə', 't eɪ k', 'h ɪ z', 'k l əʊ k', 'ɒ f', 'ʃ ʊ d', 'b i', 'k ə n s ɪ d ə d', 's t r ɒ ŋ ɡ ə', 'ð ə n', 'ð i', 'ʌ ð ə', 'ð e n', 'ð ə', 'n ɔː θ', 'w ɪ n d', 'b l uː', 'ə z', 'h ɑː d', 'ə z', 'i', 'k ʊ d', 'b ə t', 'ð ə', 'm ɔː', 'h i', 'b l uː', 'ð ə', 'm ɔː', 'k l əʊ s l i', 'd ɪ d', 'ð ə', 't r æ v l ə', 'f əʊ l d', 'h ɪ z', 'k l əʊ k', 'ə r aʊ n d', 'h ɪ m' ]
consmap = {
#   IPA	 3POA				4MOA			5VOI
    'g': ['velar',			'plosive',		1],
    'b': ['bilabial',		'plosive',		1],
    'tʃ':['post-alveolar',	'affricate',	0],
    'd': ['alveolar',		'plosive',		1],
    'ð': ['dental',			'fricative',	1],
    'f': ['labio-dental',	'fricative',	0],
    'ɡ': ['velar',			'plosive',		1],
    'h': ['glottal',		'fricative',	0],
    'dʒ':['post-alveolar',	'affricate',	1],
    'k': ['velar',			'plosive',		0],
    'l': ['alveolar',		'approximant',	1],
    'm': ['bilabial',		'nasal',		1],
    'n': ['alveolar',		'nasal',		1],
    'ŋ': ['velar',			'nasal',		1],
    'p': ['bilabial',		'plosive',		0],
    'r': ['post-alveolar',	'approximant',	1],
    's': ['alveolar',		'fricative',	0],
    'ʃ': ['post-alveolar',	'fricative',	0],
    't': ['alveolar',		'plosive',		0],
    'θ': ['dental',			'fricative',	0],
    'v': ['labio-dental',	'fricative',	1],
    'w': ['labio-velar',	'approximant',	1],
    'j': ['palatal',		'approximant',	1],
    'z': ['alveolar',		'fricative',	1],
    'ʒ': ['post-alveolar',	'fricative',	1]
}

#solution
dic = {}
i = 0
for i in range(len(esop)-1): #we have to subtract 1 because we look one word ahead, otherwise index out of range on the last word
    if esop[i][-1] in consmap and esop[i+1][0] in consmap:
        if consmap[esop[i][-1]][2] == 0 and consmap[esop[i+1][0]][2] == 1:
            print(esop[i],' ',esop[i+1])
    i += 1