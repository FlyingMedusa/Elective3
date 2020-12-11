#    produkt  model  cena   sztuk  na magazynie
a = 'robot    r2d2   89.50  12     True'
b = [str,     str,   float, int,   bool]

#solution
alist = a.split()
i = 0
for i in range(len(alist)):
    if isinstance(alist[i], b[i]):
        print(alist[i], type(str(b[i])))
    else:
        if alist[i].isnumeric():
            print(alist[i],type(int(alist[i])))
        elif alist[i] == 'True' or alist[i] == 'False':
            print(alist[i],type(bool(alist[i])))
        else:
            print(alist[i],type(float(alist[i])))