# Исходные данные: есть склад размером 30 на 40 и высотой 20,
# размер коробки – 5 х 8 х 4. Напишите программу, которая
#    сохраняет эти данные в переменных, вычисляет и выводит в консоль,
#    сколько коробок поместится на склад. В программе
#    должна быть отдельная функция, которая вычисляет и возвращает объём
#    (независимо от того, объём чего вычисляется, коробки или
#    склада).

def calculate_square(length, width, height):
    square = length * width * height
    return square


storage_length = 30
storage_width = 40
storage_height = 20
box_length = 5
box_width = 8
box_height = 4

storage_square = calculate_square(storage_length, storage_width, storage_height)
box_square = calculate_square(box_length, box_width, box_height)
boxes = int(storage_square / box_square)

print("Storage can carry ", boxes, "boxes")

