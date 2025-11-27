# Напишите программу, которая запрашивает у пользователя,
# какая сейчас температура. Выведите в
#    консоль в зависимости от температуры одну из следующих фраз:
#    - "На улице холодно!" - если температура ноль градусов или ниже
#    - "На улице прохладно" - если температура от 1 до 20 градусов включительно
#    - "На улице тепло" - если температура от 21 до 30 градусов включительно
#    - "На улице жарко!" - если температура выше 30 градусов

temperature = float(input("Enter a temperature: "))

# if temperature <= 0:
#     print("It's cold outside!")
# elif 1 <= temperature <= 20:
#     print("It's cool outside!")
# elif 21 <= temperature <= 30:
#     print("It's warm outside!")
# else:
#     print("It's hot outside!")

if temperature <= 0:
    print("На улице холодно!")
elif temperature <= 20:
    print("На улице прохладно")
elif temperature <= 30:
    print("На улице тепло")
else:
    print("На улице жарко!")