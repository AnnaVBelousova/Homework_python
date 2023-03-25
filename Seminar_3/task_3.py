# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456

def user_data(name, birthday, place_of_birth, mail, phone):
    return name, birthday, place_of_birth, mail, phone

name ="Иван Иванов" 
birthday = "1946 года рождения" 
place_of_birth = "Москва" 
mail = "email: jackie@gmail.com"
phone ="телефон: 01005321456"

data = user_data(name, birthday, place_of_birth, mail, phone)
print (f'{data[0]} {data[1]}, проживает в городе {data[2]}, {data[3]}, {data[4]}')