# Исходные данные: есть длина и ширина погрузочного пространства корабля,
# а также длина и ширина морского контейнера.
# В программе ввода, которая запрашивает эти данные у пользователя,
# сохраняет эти данные в запросе, вычисляет и выводит в консоль, сколько контейнеров можно перевезти.

shipLength = float(input("Enter the length of the ship's loading space: "))
shipWidth = float(input("Enter the width of the ship's loading space: "))
containerLength = float(input("Enter the length of the sea container: "))
containerWidth = float(input("Enter the width of the sea container: "))

shipArea = shipLength * shipWidth
containerArea = containerLength * containerWidth
countOfContainers = int(shipArea / containerArea)

print("This ship can carry ", countOfContainers, " containers")