# Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
# Подсказка:
# На каждом шаге вам нужно 'доставать' из числа очередную цифру
# и смотреть является ли она четной или нечетной.
# При этом увеличиваем соответствующий счетчик
# Пока все числа не извлечены, рекурсивные вызовы продолжаем
# Условие завершения рекурсии - все числа извлечены
# Используем операции % //. Операции взятия по индексу применять нельзя.
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите число: 123
# Количество четных и нечетных цифр в числе равно: (1, 2)



# def count_numbers (N):
    
#     last = N%10
#     count1 = 0
    
  
   

#     if last % 2==0:
#         count1+=1
     
    
  
#     if  N//10==0:
#         return count1
       
#     return count1, count_numbers(N%10)

# N = int(input("Введите число:"))
# res = count_numbers(N)
# print(res)

# Number_as_string = str(N)
# length_N =len(Number_as_string)




# print (*res)


def count_numbers (N, count_even, count_odd):
    if N//10 == 0:
        return count_even, count_odd
    count_even = 0
    count_odd = 0
    else: N%10%2 == 0
        count_even +=1
    if N%10%2 == 1:
        count_odd +=1
    
        
        
    return count_numbers (N//10, count_even, count_odd) 

N = int(input("Введите число:"))
result = count_numbers(N,0,0)
    
   
    
    
    

     
    
  
    if  N//10==0:
        return n
       
    return  count_numbers( N//10)

N = int(input("Введите число:"))
res = count_numbers(N)
print(res)

Number_as_string = str(N)
length_N =len(Number_as_string)









        
#     if index == length_N:
        
#         return lst
       
#     return res, index+1

# result = counting_even_odd(res)
# print(result)









