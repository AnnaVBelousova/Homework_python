# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.

# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# # Результат через словарь: Осень


month = int(input("Введите месяц :"))
list_month = [1,2,3,4,5,6,7,8,9,10,11,12]
if month in list_month[0:2] or month  == list_month[11]:
    season = "Зима"
elif month in list_month[2:5]:
    season = "Весна"
elif month in list_month[5:8]:
    season = "Лето"
else: season = "Осень"
print(season)


month = int(input("Введите месяц :"))
my_dict = { "Зима":[12,1,2],"Весна":[3,4,5], "Лето":[6,7,8],"Осень":[9,10,11]}
for k,v in my_dict.items():
    if month in v: 
        print(k)
