# Marta Sleboda - ex. h

consmap = {
#   IPA	 3POA				4MOA			5VOI
    'g': ['velar',			'plosive',		1],
    'b': ['bilabial',		'plosive',		1],
    'tʃ':['post-alveolar',	'affricate',	0],
    'd': ['alveolar',		'plosive',		1],
    'ð': ['dental',			'fricative',	1],
    'f': ['labio-dental',	'fricative',	0],
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

def result(good, bad):
    return int(good/(good+bad)*100)

POA_abbr_dict = {consmap[key][0]: (str(consmap[key][0])[:2] if str(consmap[key][0]).startswith('la') == False else str(consmap[key][0])[:7]) for key in consmap}
abbr_opposite = {POA_abbr_dict[key]: key for key in POA_abbr_dict}

print("Use the following POA codes:")
for key in POA_abbr_dict:
    print(key + ":", POA_abbr_dict[key])

good = 0
bad = 0
for phoneme in consmap:
    correct = False
    while correct == False:
        answer = str(input("\nThe POA of the /" + phoneme + "/ phoneme is:"))
        while True:
            try:
                unabbr = abbr_opposite[answer]
                break
            except KeyError as e:
                print("It's not a proper abbrieviation!")
                answer = str(input("\nThe POA of the /" + phoneme + "/ phoneme is:"))
        unabbr = abbr_opposite[answer]
        if unabbr == consmap[phoneme][0]:
            print("Correct!", "/" + phoneme + "/ is", unabbr + "!" )
            correct = True
            good += 1
        else:
            print("Wrong, try again")
            bad += 1

print("Your score:", good, "answers and", bad, "bad answers.", "It's exactly", round(result(good, bad),1), "%")