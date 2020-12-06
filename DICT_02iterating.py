# to go through the elements in your dict, you can use the 'for loop'
owoce_dict = {'jabłko': 'apple', 'banan': 'banana', 'truskawka': 'strawberry', 'pomarańcza': 'orange', 'awokado': 'avocado'}

'''
The structure:
for key(you can call it differently, as you wish) in dictionary_name:
    and if you want to print the key:
    print(key)
    if you want to print the value:
    print(dictionary_name[key])
    if you want to print both:
    print(key, dictionary_name[key])
'''
for key in owoce_dict:
    print(key, 'means', owoce_dict[key])

print('  *************************')

# you can add some conditions:
for key in owoce_dict:
    # if the first letter is one of the vowels
    if owoce_dict[key][0] in 'aeiouy':
        print(key, 'means an', owoce_dict[key])
    # otherwise:
    else:
        print(key, 'means a', owoce_dict[key])