# Напишите программу, перемножающую чётные числа, которые вводит пользователь.
# Программа должна перемножить любое количество чётных чисел, которое введёт пользователь.
# Ввод должен быть остановлен, если пользователь введёт ноль,
# после этого должен быть отображён на экране результат умножения.

number = int(input("Enter a number: "))
result = 1

while number != 0:
    if number % 2 == 0:
        result *= number

    number = int(input("Enter a number: "))

print("Result: ", result)

# result = 1
#
# while True:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break
#
#     if number % 2 == 0:
#         result *= number
#
# print("Result: ", result)
