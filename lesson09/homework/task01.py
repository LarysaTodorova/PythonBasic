# Напишите функцию, которой можно передать целое число.
# Функция должна возвращать True, если число попадает в диапазон от 10 до 30 включительно.
# В остальных случаях функция должна возвращать False.
# Вызовите функцию несколько раз, передав ей различные аргументы, и выведите результаты в консоль.

def is_pass_an_integer(number):
    num1 = number >= 10
    num2 = number <= 30
    return num1 and num2

print(is_pass_an_integer(9))
print(is_pass_an_integer(10))
print(is_pass_an_integer(11))
print(is_pass_an_integer(29))
print(is_pass_an_integer(30))
print(is_pass_an_integer(31))
