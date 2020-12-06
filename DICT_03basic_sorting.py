owoce_dict = {'jabłko': 'apple', 'banan': 'banana', 'truskawka': 'strawberry', 'pomarańcza': 'orange', 'awokado': 'avocado', 'cytryna': 'lemon'}

# Sorting a dictionary by keys from A-Z (or from smallest to largest)
print(sorted(owoce_dict))

print('  *************************')

# SORTING IN A LOOP

# Sorting a dictionary by keys from Z-A (or from largest to smallest)
# for key in sorted(dictionary_name, reverse=True):
for key in sorted(owoce_dict, reverse=True):
    print(key, owoce_dict[key])

print('  *************************')
# Sorting a dictionary by VALUES from A-Z (use an expression: key = lambda x: dictionary_name[x])
for key in sorted(owoce_dict, key = lambda x: owoce_dict[x]):
    print(key, owoce_dict[key])

print('  *************************')
# Sorting a dictionary by VALUES from Z-A (use an expression: key = lambda x: dictionary_name[x] and reverse=True)
for key in sorted(owoce_dict, key = lambda x: owoce_dict[x], reverse=True):
    print(key, owoce_dict[key])