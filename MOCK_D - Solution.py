esop = [ 'ð ə', 'n ɔː θ', 'w ɪ n d', 'ə n', 'ð ə', 's ʌ n', 'w ə', 'd ɪ s p j u t ɪ ŋ', 'w ɪ tʃ', 'w ə z', 'ð ə', 's t r ɒ ŋ ɡ ə', 'w e n', 'ə', 't r æ v l ə', 'k eɪ m', 'ə l ɒ ŋ', 'r æ p t', 'ɪ n', 'ə', 'w ɔː m', 'k l əʊ k', 'ð eɪ', 'ə ɡ r iː d', 'ð ə t', 'ð ə', 'w ʌ n', 'h u', 'f ɜː s t', 's ə k s i d ɪ d', 'ɪ n', 'm eɪ k ɪ ŋ', 'ð ə', 't r æ v l ə', 't eɪ k', 'h ɪ z', 'k l əʊ k', 'ɒ f', 'ʃ ʊ d', 'b i', 'k ə n s ɪ d ə d', 's t r ɒ ŋ ɡ ə', 'ð ə n', 'ð i', 'ʌ ð ə', 'ð e n', 'ð ə', 'n ɔː θ', 'w ɪ n d', 'b l uː', 'ə z', 'h ɑː d', 'ə z', 'i', 'k ʊ d', 'b ə t', 'ð ə', 'm ɔː', 'h i', 'b l uː', 'ð ə', 'm ɔː', 'k l əʊ s l i', 'd ɪ d', 'ð ə', 't r æ v l ə', 'f əʊ l d', 'h ɪ z', 'k l əʊ k', 'ə r aʊ n d', 'h ɪ m' ]
vowmap = {
    #IPA  PAL			EX
    'iː': ['palatal',	'bean'], 
    'ɑː': ['',			'barn'], 
    'ɜː': ['',			'bird'], 
    'ɛː': ['',			'pair'], 
    'ɔː': ['',			'born'], 
    'uː': ['',			'boon'],

    'i':  ['palatal',	'happy'], 
    'ɪ':  ['palatal',	'pit'],  
    'u':  ['',			'you'], 
    'ʌ':  ['',			'putt'],
    'æ':  ['',			'pat'],  
    'ə':  ['',			'about'],  
    'e':  ['',			'pet'],  
    'ɒ':  ['',			'pot'],  
    'ʊ':  ['',			'good'],  

    'ɪə': ['palatal',	'peer'],
    'eɪ': ['palatal',	'face'],  
    'aɪ': ['palatal',	'buy'], 
    'ɔɪ': ['palatal',	'boy'], 
    'aʊ': ['',			'now'], 
    'oʊ': ['',			'no'],
    'əʊ': ['',			'no'],
    'ʊə': ['',			'poor'], 
    'eə': ['',			'pair']
}

#solution
palatals = vowels = consonants = 0
for word in esop:
    for phon in word.split():
        if phon in vowmap:
            vowels += 1
            if vowmap[phon][0]=='palatal':
                palatals += 1
        else:
            consonants += 1
print('The text \'esop\' contains', vowels, 'vowels including', palatals, 
      'palatal ones, palatals therefore constitute', str(round((palatals/(vowels))*100,2)) +
      '%. In the text, there are', consonants, 'consonants, which constitute',
      str(round((consonants/(consonants+vowels))*100,2)) + '% of all phonemes.')