# Напишите программу, которая запрашивает у пользователя число.
# Программа должна вывести на
#    экран одно из трёх сообщений – «Ваше число отрицательное»,
#    «Ваше число равно нулю», «Ваше число положительное».

user_number = int(input("Enter the number: "))

if user_number < 0:
    print("Your number is negative")
elif user_number == 0:
    print("Your number is zero")
else:
    print("Your number is positive")
