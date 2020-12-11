consmap = {
#   IPA	 POA				POAabbr	MOA				MOAabbr	5VOI
    'b': ['bilabial',		'b',	'plosive',		'p',	1],
    'd': ['alveolar',		'a',	'plosive',		'p',	1],
    'ɡ': ['velar',			'v',	'plosive',		'p',	1],
    'p': ['bilabial',		'b',	'plosive',		'p',	0],
    't': ['alveolar',		'a',	'plosive',		'p',	0],
    'k': ['velar',			'v',	'plosive',		'p',	0]
}

#solution

i = 0
poa = {}
moa = {}
for c in consmap:
    if consmap[c][0] not in poa:
        poa[consmap[c][0]] = consmap[c][1]
print('Use the following POA codes:',poa)

i = 'start'
correct = 0
wrong = 0
for c in consmap:
    i = input('What is the POA of /' + c + '/ ? Type POA code.')
    while i != consmap[c][1]:
        wrong += 1
        i = input('  Wrong, try again: (' + str(correct) +':'+ str(wrong) + ')')
    else:
        correct += 1
        print('Correct, /' + c + '/ is ' + consmap[c][0] + '! (' + str(correct) +':'+ str(wrong) + ')')
print('Your score is ' + str(correct) +':'+ str(wrong) + ' i.e. ' + str(round(correct/(correct+wrong)*100, 2)) + '%.')