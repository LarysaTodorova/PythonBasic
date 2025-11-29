# Доработайте вторую задачу таким образом, чтобы у пользователя было только пять попыток ввода.
# После пятой некорректной попытки программа должна завершаться с сообщением
# "Ошибка регистрации!".

input_number = 5

for i in range(input_number):
    password = input("Enter a password: ")

    if len(password) >= 8:
        break

else:
    print("Registration error!")
