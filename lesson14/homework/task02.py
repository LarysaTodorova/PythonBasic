# Создайте список, который состоит из нескольких положительных чётных и нечётных целых чисел.
# Напишите программу, которая определяет и выводит на экран максимальное из чётных чисел списка.

numbers = [5, 9, 7, 0, 2, 6, 16]
max_number = 0

for number in numbers:
    if number > max_number and number % 2 == 0:
        max_number = number
        continue

print(max_number)

