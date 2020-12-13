
'''
6.2f – przeznacz 6 znaków na zapisanie liczby zmiennoprzecinkowej, z czego 2 będą po kropce
%14s – przeznacz 14 znaków na zapisanie string’a
%10s – przeznacz 10 znaków na zapisanie string’a
'''


my_list = [[2.7485,"Usain Bolt", "16.08.2009"],[3.879374975, "Bill Gates", "04.12.2020"], [1.2, "Sheldon Cooper", "21.02.1998"]]

width = 40
print()
print("-" * width)
print("|  Time  |     Player     |    Date    |")
print("*" * width)
i = 0
for el in my_list:
    print("| {:6.2f} | {:14s} | {:10s} |" .format(my_list[i][0], my_list[i][1], my_list[i][2]))
    i += 1
    if i == len(my_list):
        break
print("-" * width, "\n")

