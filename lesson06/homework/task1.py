# Исходные данные: два числа – 37 и 16. Сохраните эти данные в двух переменных.
# Напишите функцию с двумя параметрами, которая считает разность двух чисел.
# При помощи функции посчитайте разность и выведите в консоль: первого и второго числа,
# первого и первого числа, второго и второго числа.
# Затем вызовите функцию, но передайте в качестве аргументов не переменные, а два любые числа.

def subtraction(value_1, value_2):
    difference1 = value_1 - value_2
    difference2 = value_1 - value_1
    difference3 = value_2 - value_2
    return difference1, difference2, difference3


number_1 = 37
number_2 = 16

print(subtraction(number_1, number_2))
print(subtraction(50, 25))