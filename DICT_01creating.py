# Dictionaries: unordered collections of key-value pairs

# Examples below
dictionary = {'key': 'value'}
a_plen_dict = {'jabłko': 'apple', 'banan': 'banana', 'truskawka': 'strawberry'}
body_parts = {'legs': 2, 'head': 1, 'fingers': 10, 'arms': 2, 'eyes': 2, 'heart': 1}
# Keys have to be UNIQUE, values can be repeated

# Adding keys and values to a dictionary
# 1. Creating an empty or somehow filled dicionary
english_polish_dict = {}

# 2. To add sth to a dict you need the following structure:
#    dict_name['key'] = value
english_polish_dict['dog'] = 'pies'
english_polish_dict['cat'] = 'kot'
english_polish_dict['mouse'] = 'mysz'

# 3. Now your dictionary has three keys and three values
print(english_polish_dict)