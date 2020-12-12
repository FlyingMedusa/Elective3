dic = {'dom': ['house', 'home', 'casa'], 'choinka': ['Christmas tree', 'holiday tree'], 'Święta Bożego Narodzenia': ['Christmas', 'Xmas', 'Noel'], 'przerwa świąteczna': ['Christmas break', 'holiday break', 'summer holidays']}

#solution
j = 1
dicc = []
print('Input dictionary:')
for i in dic:
    print(j,i,end=': ')
    for k in dic[i]:
        print(k, end='  ')
    dicc.append(i)                   #new dictionary with numbers as keys and keys of dic as values
    print()
    j+=1

x = input('\nDo you want to remove equivalents from any of these entries? [y]: ')    

while x == 'y':
    y = input('Give the number of the entry you want to remove an equivalent from. [1-' + str(len(dic)) + ']: ')

    #test input
    if y.isnumeric(): 
        y = int(y)
    else:
        print('Wrong value'); break
    if y < 1 or y > len(dic): print('Wrong value'); break
        
    n = 1
    for m in dic[dicc[y-1]]:
        print(n,m,end='  ')
        n+=1
    print()
    p = 'y'
    while p == 'y':
        if len(dic[dicc[y-1]]) > 0:
            o = input('Give the number of the equivalent you want to remove. [1-' + str(len(dic[dicc[y-1]])) + ']: ')

            #test input
            if o.isnumeric(): 
                o = int(o)
            else:
                print('Wrong value'); break
            if o < 1 or o > len(dic[dicc[y-1]]): print('Wrong value'); break

            print('You successfully removed:', dic[dicc[y-1]].pop(o-1)+'.')
            if len(dic[dicc[y-1]]) == 0:
                continue
            p = input('Do you want to remove another equivalent from the entry? [y]: ')
            s = 1
            for r in dic[dicc[y-1]]:
                print(s, r, end='  ')
                s += 1
            print()
        else:
            print('There are no more equivalents for', dicc[y-1])
            break
    x = input('\nDo you want to remove equivalents from any of these entries? [y]: ')    

print('\nOutput dictionary:\n', dic)