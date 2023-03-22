# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).

# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!

# Process finished with exit code 0

# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0

# Process finished with exit code 0

one_number = int(input("Введите число:"))
second_number = int(input("Введите число:"))

def divizion (a, b):
    return a/b 
result = divizion(one_number, second_number)
print(result)
