# Напишите функцию, которой можно передать целое число.
# Функция должна возвращать True, если число положительное чётное
#    либо отрицательное. В остальных случаях функция должна возвращать False.
#    Вызовите функцию несколько раз, передав ей
#    различные аргументы, и выведите результаты в консоль.

# Примеры:
# True: 6, 14, 22, -4, -17, -25
# False: 7, 19, 1, 0

def is_positive_even_or_negative(number):
    is_positive = number > 0
    is_even = number % 2 == 0
    is_negative = number < 0
    is_positive_even = is_positive and is_even
    return is_negative or is_positive_even

print(is_positive_even_or_negative(6))
print(is_positive_even_or_negative(14))
print(is_positive_even_or_negative(22))
print(is_positive_even_or_negative(-4))
print(is_positive_even_or_negative(-17))
print(is_positive_even_or_negative(-25))
print(is_positive_even_or_negative(7))
print(is_positive_even_or_negative(19))
print(is_positive_even_or_negative(1))
print(is_positive_even_or_negative(0))