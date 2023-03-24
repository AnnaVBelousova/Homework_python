# ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ:
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
def my_list(N):
    list_1 = []
    for i in range(N):
        n  = int(input("введите число n = "))
        list_1.append(n)
    return list_1


def element_number(list_1):
    x = int(input("введите число х = "))
    count = 0
    for el in list_1:
    
        if el == x:
            count = count+1 
    return count

N  = int(input("введите число:"))


mylist = my_list(N)
print(mylist)
repetition_number = element_number(mylist)
print(repetition_number)
    
