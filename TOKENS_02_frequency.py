sentence = "Now you people have names . That's because you don't know who you are . We know who we are, so we don't need names ."
# firstly let's split the sentence into words by spaces, now we don't have a string but a list
sentence = sentence.split()

freq_dict = {}   #create an empty dictionary before the loop
for word in sentence:
    if word.lower() in freq_dict:
        freq_dict[word.lower()] += 1
    else:
        freq_dict[word.lower()] = 1

print(freq_dict, '\n')
'''
So basically we check whether we have a word in our dictionary: if not, then add it with a value '1'
but if we have a word there, then we increment its value by '1'

And if you want to present the frequency from the most common words to the least common ones
then you need to loop through your sorted dictionary (remember to sort by valuse so use the lambda expression)
'''
for key in sorted(freq_dict, key = lambda x: freq_dict[x], reverse=True):
    print(key, '-',freq_dict[key])



# you can also choose the 'top 10 version'
print('  *************************\nTOP 10:')
counter = 0
for key in sorted(freq_dict, key = lambda x: freq_dict[x], reverse=True):
    counter += 1
    if counter <= 10:
        print(str(counter) + '.\t', key, '-',freq_dict[key])
    else:
        break
