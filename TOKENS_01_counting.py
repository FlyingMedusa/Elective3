sentence = "Now you people have names . That's because you don't know who you are . We know who we are, so we don't need names ."
# firstly let's split the sentence into words by spaces, now we don't have a string but a list
sentence = sentence.split()

# counting the number of words/punctuation
print('All elements:', len(sentence))

# counting tokens - we create a set with unique elements, however here it considers 'We' and 'we' as separate tokens
print('Case-sensitive tokens:', len(set(sentence)))

''' 
counting tokens in a case-insensitive way (so 'We' and 'we' will be one token)
the easiest way is to create the same sentence using lower()
'''
lowered_sentence = [word.lower() for word in sentence]
print('Case-insensitive tokens:', len(set(lowered_sentence)))