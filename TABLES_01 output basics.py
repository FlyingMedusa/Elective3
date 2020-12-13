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

i = 1
print('\n{:<5}{:<5}{:<20}{:<20}{:<5}\n'.format("","IPA","POA","MOA","VOI"))
for key in sorted(consmap, key = lambda x: consmap[x]):
    print('{:<5}{:<5}{:<20}{:<20}{:<5}'.format(i, key, consmap[key][0], consmap[key][1], consmap[key][2]))
    i += 1