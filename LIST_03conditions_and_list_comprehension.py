# here we want to create a list out of names that start with 'A'

all_names = ['Marta', 'Amber', 'Philip', 'Veronica', 'Alex', 'Alice', 'Nicolas', 'Anastasia', 'Noelle', 'Jamie', 'Joe', 'Angellica']

new_list = [name for name in all_names if name.startswith('A')]
print(new_list)


print('  *************************')
# now a list out of names that consist of maximum 5 characters, and we want to capitalize them

short_names = [a_name.capitalize() for a_name in all_names if len(a_name) <= 5]
print(short_names)