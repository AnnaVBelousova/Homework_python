# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()
res = 0
a  = int(input())
b = int(input())
c = int(input())
def my_func (a, b ,c):
    if a-b>0 and a -c > 0:
        a = max
        if b>c:
             a + b == res
        else: 
             a + c== res
    elif a - b < 0 and b-c >0:
        b = max
        if a>c:
             a + b == res
        else: 
             b + c== res
    else: 
        c = max
        if b>a:
             c + b== res 
        else: 
            a + c== res
    return res
result = my_func(int(input("введите число:")), int(input("введите число:")), int(input("введите число:")))
print(result)
   
    
