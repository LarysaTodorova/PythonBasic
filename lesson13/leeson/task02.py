# Напишите программу, которая суммирует числа, которые вводит пользователь.
# Программа должна просуммировать любое
#    количество чисел, которое введёт пользователь.
#    Ввод должен быть остановлен, если пользователь введёт ноль, после
#    этого должен быть отображён на экране результат суммирования.

summa = 0

# while True:
#     user_number = int(input("Enter a number: "))
#     if user_number == 0:
#         print("Result: ", summa)
#         break
#     summa += user_number

while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    summa += number

print("Результат суммирования -", summa)
