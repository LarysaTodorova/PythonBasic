# Напишите программу, которая запрашивает у пользователя его имя, возраст и город проживания,
# а затем формирует приветственное сообщение с использованием функций и конкатенации строк.
# Создайте функцию get_user_info(), которая будет:
# а. Запрашивать у пользователя его имя, возраст и город и сохранять эти данные в переменных.
# б. Вызывать функцию generate_greeting(name, age, city), которая в свою очередь будет:
# Выводить на экран приветственное сообщение, используя конкатенацию строк.

def generate_greeting(name, age, city):
    print("Hello, my name is " + name + ". I am " + age + ", and I live in " + city + ".")


def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    generate_greeting(name, age, city)


get_user_info()