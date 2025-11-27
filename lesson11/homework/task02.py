# Напишите программу, которая запрашивает у пользователя три числа.
# Напишите функцию, которая выводит на экран фразу "Сумма трёх чисел положительная и чётная",
# если это так. Для всех остальных случаев функция должна просто выводить сумму трёх чисел на экран.

def print_sum(num1, num2, num3):
    summa = num1 + num2 + num3
    if summa >= 0 and summa % 2 == 0:
        print("The sum of three numbers is positive and even.")
    else:
        print(summa)


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

print_sum(first_number, second_number, third_number)
