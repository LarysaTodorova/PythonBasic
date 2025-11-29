# Запросите у пользователя два числа.
# Напишите программу, которая суммирует все числа в диапазоне
# от первого до второго
#    и выводит результат на экран.
#    Например, пользователь ввёл 5 и 8.
#    Программа должна посчитать 5 + 6 + 7 + 8 и вывести
#    результат на экран.

start = int(input("Enter start diapason: "))
end = int(input("Enter end number diapason: "))

summa = 0

while start <= end:
    summa += start
    start += 1

print("Result: ", summa)
