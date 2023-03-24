
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
def my_list(N):
    list_1 = []
    for i in range(N):
        n  = int(input("введите число n = "))
        list_1.append(n)
    return list_1


def the_most_closed_number(list_1):
    x = int(input("введите число х = "))

    differences = []
    for el in list_1:
        modul = abs(x-el)
        differences.append(modul)
    
    minvalue = min(differences)
    index = differences.index(minvalue)
            
    return list_1[index]

try:
    N  = int(input("введите число:"))
    mylist = my_list(N)
    print(mylist)
    the_most_closed = the_most_closed_number(mylist)
    print(the_most_closed)
except ValueError:
    print('это не число!')
