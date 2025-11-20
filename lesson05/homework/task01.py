# Исходные данные: есть количество рядов сидений в салоне самолёта,
# количество сидений в каждом ряду, а также количество пассажиров,
# которые купили билет на этот самолёт.
# Напишите программу,
# которая запрашивает эти данные у пользователя, сохраняет эти данные в переменных,
# вычисляет и выводит в консоль, сколько свободных мест осталось в самолёте.


numberOfRows = int(input("Enter the number of rows in the plane: "))

numberOfSeats = int(input("Enter the number of seats in the plane: "))

numberOfPassengers = int(input("Enter the number of passengers who purchased a ticket for this flight: "))

countOfFreeSeats = numberOfRows * numberOfSeats - numberOfPassengers

print("On the plane left ", countOfFreeSeats, " free seats.")