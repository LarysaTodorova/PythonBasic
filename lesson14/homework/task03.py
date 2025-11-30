# Напишите функцию, которая принимает на вход список чисел,
# находит в нём максимальное и минимальное значения, и меняет их местами.

def change_numbers(numbers):
    min_index = 0
    max_index = 0

    for i in range(len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
        if numbers[i] > numbers[max_index]:
            max_index = i
        continue

    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    return numbers

list_numbers = [5, 9, -7, 0, -2, 6, -16]
print(change_numbers(list_numbers))
