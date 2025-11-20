# Напишите программу, которая поможет клиенту контролировать стоимость покупок.
# Программа должна запросить у пользователя название товара, его цену и количество.
# В конце она должна вывести итоговую стоимость каждой покупки и общую стоимость всех покупок
# с помощью строки конкатенации.
# Товара только два — следует учитывать, что большее количество товаров не требуется.

productName = input("Enter the first product name: ")
productPrice = float(input("Enter the first product price: "))
productQuantity = int(input("Enter the first product quantity: "))
totalFirstProductPrice = productPrice * productQuantity

secondProductName = input("Enter the second product name: ")
secondProductPrice = float(input("Enter the second product price: "))
secondProductQuantity = int(input("Enter the second product quantity: "))
totalSecondProductPrice = secondProductPrice * secondProductQuantity

totalPrice = totalFirstProductPrice + totalSecondProductPrice

print("Total price " + productName + ": " + str(totalFirstProductPrice) + " euro")
print("Total price " + secondProductName + ": " + str(totalSecondProductPrice) + " euro")
print("Total price of all purchases: " + str(totalPrice) + " euro")

