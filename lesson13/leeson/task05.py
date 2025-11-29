# Напишите программу, которая суммирует все числа в диапазоне
# от первого до второго
#    и выводит результат на экран.
#    Например, пользователь ввёл 5 и 8.
#    Программа должна посчитать 5 + 6 + 7 + 8 и вывести
#    результат на экран.

start = int(input("Enter start diapason: "))
end = int(input("Enter end number diapason: "))

summa = 0

for i in range(start, end + 1):
    summa += i

print("Result: ", summa)
