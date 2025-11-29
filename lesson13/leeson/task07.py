# Правильный пароль пользователя – qwerty.
# Напишите программу, которая запрашивает пароль у пользователя.
# Причём попытки ввода должны повторяться до тех пор,
# пока пользователь не введёт правильный пароль.

# password = "qwerty"
#
# while True:
#     user_password = input("Enter your password: ")
#     if user_password == password:
#         print("Access granted!")
#         break
#     else:
#         print("Access denied!")

password = "qwerty"

user_password = ""

while user_password != password:
    user_password = input("Enter your password: ")

print("Access granted!")
