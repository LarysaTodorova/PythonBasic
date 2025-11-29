# Напиши программу:
# Пользователь вводит 10 чисел
# Нужно проверить: есть ли среди них число 7
# Если есть → вывести "Found!" и прекратить поиск (break)
# Если после всех 10 чисел не нашли → вывести "Not found!" (через for-else)

for i in range(10):
    number = int(input("Enter a number: "))

    if number == 7:
        print("Found!")
        break

else:
    print("Not Found")
