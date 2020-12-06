all_names = ['Marta', 'Amber', 'Philip', 'Veronica', 'Alex', 'Alice', 'Nicolas', 'Anastasia', 'Noelle', 'Jamie', 'Joe', 'Angellica']

# startswith()   endswith()
for name in all_names:
    if name.startswith('A') and name.endswith('a'):
        print(name, 'starts with an "A" and ends with an "a"')
    elif name.startswith('A'):
        print(name, 'starts with an "A"')
    elif name.endswith('a'):
        print(name, 'ends with an "a"')
    