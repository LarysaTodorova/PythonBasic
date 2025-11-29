# Напиши программу проверки пароля:
# правильный пароль — "python123"
# у пользователя есть 5 попыток
# если он вводит правильный пароль → вывести "Access granted!" и остановить программу
# если 5 раз ввёл неправильно → вывести "Access denied!"

password = "python123"

for i in range(5):
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access granted!")
        break

else:
    print("Access denied!")
