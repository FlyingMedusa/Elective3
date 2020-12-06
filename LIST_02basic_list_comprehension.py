# 1. a regular way of appending a list (so you can compare with list comprehension)

old_names = ['marta', 'philip', 'veronica', 'alex', 'alice', 'nicolas']
new_names = [] #here we tell a program that we will have a new list
for name in old_names:
    new_names.append(name.capitalize())

print(new_names)




print('  *************************')


# 2. same thing but with a LIST COMPREHENSION

old_surnames = ['sleboda', 'łyczywek', 'makaruk']
new_surnames = [surname.capitalize() for surname in old_surnames]

print(new_surnames)

'''
So the stucture is as follows:
name_of_a_new_list = [what_you_want_to_add for element in name_of_sth_that_you_go_through(input)]
'''