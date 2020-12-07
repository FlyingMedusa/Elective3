dic = {'dom': [], 'choinka': [], 'Święta Bożego Narodzenia': [], 'wakacje': []}

for key in dic:
    user_answ = input('Do you want a translation for "' + key + '"? (y/n)')
    if user_answ == "y":
        new_trans = input('Please enter a translation:')
        dic[key].append(new_trans)
        answ = True
        while answ == True:
            an_answ = input('Would you like to add another translation for "' + key + '"?(y/n)')
            if an_answ == "y":
                new_trans = input('Please enter a translation:')
                dic[key].append(new_trans)
                answ == True
            else:
                answ == False
                print("Oki doki moving on!")
                break
                
    else:
        continue
        
print("That's it! Here's your dictionary:\n", dic)