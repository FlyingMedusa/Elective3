esop = [ 'ð ə', 'n ɔː θ', 'w ɪ n d', 'ə n', 'ð ə', 's ʌ n', 'w ə', 'd ɪ s p j u t ɪ ŋ', 'w ɪ tʃ', 'w ə z', 'ð ə', 's t r ɒ ŋ ɡ ə', 'w e n', 'ə', 't r æ v l ə', 'k eɪ m', 'ə l ɒ ŋ', 'r æ p t', 'ɪ n', 'ə', 'w ɔː m', 'k l əʊ k', 'ð eɪ', 'ə ɡ r iː d', 'ð ə t', 'ð ə', 'w ʌ n', 'h u', 'f ɜː s t', 's ə k s i d ɪ d', 'ɪ n', 'm eɪ k ɪ ŋ', 'ð ə', 't r æ v l ə', 't eɪ k', 'h ɪ z', 'k l əʊ k', 'ɒ f', 'ʃ ʊ d', 'b i', 'k ə n s ɪ d ə d', 's t r ɒ ŋ ɡ ə', 'ð ə n', 'ð i', 'ʌ ð ə', 'ð e n', 'ð ə', 'n ɔː θ', 'w ɪ n d', 'b l uː', 'ə z', 'h ɑː d', 'ə z', 'i', 'k ʊ d', 'b ə t', 'ð ə', 'm ɔː', 'h i', 'b l uː', 'ð ə', 'm ɔː', 'k l əʊ s l i', 'd ɪ d', 'ð ə', 't r æ v l ə', 'f əʊ l d', 'h ɪ z', 'k l əʊ k', 'ə r aʊ n d', 'h ɪ m', 'n aʊ', 'ð eɪ', 'ə', 'p r aʊ d', 'h aʊ', 'iː z iː', 'ð æ t', 'w ə z', 'e v r i', 't aɪ m', 'ð eɪ', 'r ɪ f ɜː', 't u', 'ð eə', 'd iː d' ]
esop_palindromes = []

#for word in esop:
 #   esop_palindromes = word[::-1]
  #  if len(word) >= 3:
   #     if len(word) <= 5:
    #        if word[::-1] == esop_palindromes:
     #           print(word)
        
        
for word in esop:
    if len(word) >= 3:
        if len(word) <= 5:
            if word == word[::-1]:
                print(word)