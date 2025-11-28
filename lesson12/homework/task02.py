# Напишите программу, которая выводит на экран все чётные числа в порядке убывания
# из диапазона от 100 до 80.

for i in range(100, 79, -2):
    print(i)

counter = 100

while counter >= 80:
    if counter % 2 == 0:
        print(counter)
    counter -= 2
