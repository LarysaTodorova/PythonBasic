# Исходные данные: конфета стоит 3 у.е., мороженое стоит 5 у.е. Вы хотите купить 7 конфет и 3 мороженых.
# Напишите программу, которая сохраняет эти данные в переменных, вычисляет и выводит в консоль,
# сколько денег Вам потребуется.
# При этом программа должна содержать отдельную функцию, которая считает итоговую стоимость продукта,
# принимая на вход его количество и цену.
# Данной функцией нужно воспользоваться два раза для конфет и мороженого.

def price_for_one_product(count, price):
    multiplication = count * price
    return multiplication


candy_price = 3
ice_crem_price = 5
candy = 7
ice_crem = 3

print("Cost of candies: ",price_for_one_product(candy, candy_price))
print("Cost of ice cream: " ,price_for_one_product(ice_crem, ice_crem_price))

