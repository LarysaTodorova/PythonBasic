# Напиши функцию, которая принимает список чисел и:
# Находит второе по величине число
# Возвращает список, где первое (максимальное) и второе максимальное числа поменяны местами.
#   В списке могут быть отрицательные числа
#   В списке могут быть повторения
#   Функция должна работать с любыми значениями

def find_max_numbers(numbers):
    max_index = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[max_index]:
            max_index = i

    second_max_number = None
    for i in range(len(numbers)):
        if i == max_index:
            continue
        if second_max_number is None or numbers[i] > numbers[second_max_number]:
            second_max_number = i

    numbers[max_index], numbers[second_max_number] = numbers[second_max_number], numbers[max_index]

    return numbers


array_numbers = [8, -1, 100, 500, 5, 0, -6, 3]
print(find_max_numbers(array_numbers))
