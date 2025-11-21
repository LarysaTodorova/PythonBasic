# Бананы стоят 11 у.е., яблоки - 8 у.е. Вам нужно купить два килограмма бананов и три килограмма яблок.
# Сохраните все эти данные в переменных. Напишите программу, которая выводит на экран фразу
# "Для покупки Х килограммов бананов и Х килограммов яблок мне нужно Х у.е."
# В местах, где Х - нужно воспользоваться переменными.
# Напишите отдельную функцию, которая считает и возвращает стоимость продукта
# и воспользуйтесь ей два раза для расчёта стоимости яблок и бананов.

def calculate_price(price, kg):
    product_cost = price * kg
    return product_cost


def print_info(banana_kg, apple_kg, apple_total_price, banana_total_price):
    fruits_total_price = apple_total_price + banana_total_price
    print("To buy " + str(banana_kg) + " kilograms of bananas and " + str(
        apple_kg) + " kilograms of apples I need " + str(fruits_total_price) + " euros.")


apple_price = 8
apple_weight = 3
banana_price = 11
banana_weight = 2

total_apple_price = calculate_price(apple_price, apple_weight)
total_banana_price = calculate_price(banana_price, banana_weight)

print_info(apple_weight, banana_weight, total_banana_price, total_apple_price)
