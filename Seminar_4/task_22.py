# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.


import random
 
n = int(input())
m = int(input())

 
def fillarray(i):
    list_n = list(range(i))
    random.shuffle(list_n)
    return list_n

listn = fillarray(n)
listm = fillarray(m)


resultlist = listm + listn
resultlist.sort()
print (resultlist)


resultlist = list(set(resultlist))
print (resultlist)


