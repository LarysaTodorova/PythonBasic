#  Напишите программу, которая запрашивает у пользователя целое число N,
#  вычисляет первые N чисел последовательности Фибоначчи и выводит их на экран.
#  Числа Фибоначчи — это последовательность, где каждое число является суммой двух предыдущих,
#  начиная с чисел 0 и 1.

user_number = int(input("Enter a number: "))
previous_number = 0
current_number = 1
counter = 0

while counter < user_number:
    print(previous_number)
    previous_number, current_number = current_number, previous_number + current_number
    counter += 1
