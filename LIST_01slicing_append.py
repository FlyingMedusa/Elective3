'''
The first element of a list has a 0 index,
the last one has a -1 index
'''

fruits = ['banana', 'apple', 'lemon', 'watermelon', 'stawberry', 'kiwi']

print(fruits[0])      #output: banana
print(fruits[-1])     #output: kiwi
print(fruits[3])      #output: watermelon
print(fruits[1:4])    #output: ['apple', 'lemon', 'watermelon'] (this code won't print the last element: fruits[4])
print(fruits[2:-1])   #output: ['lemon', 'watermelon', 'stawberry']
print(fruits[:2])     #output: ['banana', 'apple'] (not giving the first inex = from the beginning)
print(fruits[4:])     #output: ['stawberry', 'kiwi'] (not giving the last inex = till the end)


print('  *************************')
# adding elements
# the list before:
print(fruits)

fruits.append('avocado')
fruits.append('ananas')

# look at the list now
print(fruits)