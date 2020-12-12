dic = {'dom': [], 'choinka': [], 'Święta Bożego Narodzenia': [], 'wakacje': []}

#solution
for i in dic:
    x = input('Do you want to translate the entry \"' + i + '\"? [y] ')
    if x == 'y':
        print('The translations so far include: ', end='')
        for d in dic[i]:
            print(d, end=' ')
        y = input('Do you want to add a translation to the above? [y] ')
        while y == 'y':
            entry = input('Give translation: ')
            dic[i].append(entry)
            print('The translations so far include: ', end='')
            for d in dic[i]:
                print(d, end=' ')       
            y = input('\nDo you want to add more translation? [y] ')
    else:
        break
print(dic)