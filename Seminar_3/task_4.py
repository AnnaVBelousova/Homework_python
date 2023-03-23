# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()
def my_func (a, b ,c):
    numbers = [a,b,c]
    numbers.sort()
    res = numbers[2]+numbers[1]
    return res
   
result = my_func(int (input("введите число:" )), int (input("введите число:" )), int (input("введите число:" )))
print(result)  

def my_func (a, b ,c):
   
    numbers = [a,b,c]
   
    maxvalue = max(numbers)
    numbers.remove(maxvalue)
    for i in range (2):
        if numbers[0]<numbers[1]:
            res = numbers[1]+maxvalue 
        else: res = numbers[0]+maxvalue
        
    return res


   
result = my_func(int (input("введите число:" )), int (input("введите число:" )), int (input("введите число:" )))
print(result)   



