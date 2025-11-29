# Напишите программу, которая принимает числа от пользователя,
# затем выводит сумму всех положительных чисел.
# Если пользователь вводит число 0,
# программа завершает ввод данных и выполняет расчёты.

summa = 0

while True:
    user_number = int(input("Enter a number: "))
    if user_number > 0:
        summa += user_number
    elif user_number == 0:
        break

print("Result: ", summa)
