# Напишите программу, которая запрашивает у пользователя число.
# Если введённое число делится нацело на три, вывести на экран – «Ваше число делится на три».
# Если нет – вывести на экран – «Ваше число не делится на три».

number  = input("Enter a number: ")

if int(number) % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

