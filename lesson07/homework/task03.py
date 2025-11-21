# Напишите программу, которая помогает пользователю рассчитать общую стоимость поездки на автомобиле.
# Программа должна запрашивать у пользователя информацию о расстоянии до пункта назначения,
# расходе топлива на 100 км, цене топлива за литр и выводить итоговую стоимость поездки.
# Программа должна использовать функции и конкатенацию строк. Создайте функцию get_trip_info(), которая будет:
# а. Запрашивать у пользователя расстояние до пункта назначения (в км),
# расход топлива на 100 км (в литрах) и цену топлива за литр.
# б. Сохранять эти данные в отдельные переменные.
# в. Вызывать функцию calculate_fuel_cost(distance, fuel_consumption, fuel_price), которая будет:
# Возвращать общую стоимость топлива для поездки.
# Затем функция get_trip_info() должна вызвать функцию
# generate_trip_report(distance, fuel_consumption, fuel_price, total_cost),
# которая будет: Выводить отчёт о стоимости поездки, используя конкатенацию строк.

def get_trip_info():
    distance = float(input("Please, enter the distance in kilometers: "))
    consumption = float(input("Please, enter the consumption per 100 km : "))
    price = float(input("Please, enter the price per liter: "))

    total_cost = calculate_fuel_cost(distance, consumption, price)

    generate_trip_report(distance, consumption, price, total_cost)


def calculate_fuel_cost(distance, fuel_consumption, fuel_price):
    return (distance / 100) * fuel_consumption * fuel_price


def generate_trip_report(distance, fuel_consumption, fuel_price, total_cost):
    print("Distance to destination: " + str(distance) + "\n"
          "Fuel consumption: " + str(fuel_consumption) + "\n"
          "Fuel price: " + str(fuel_price) + "\n"
          "Total fuel cost for the trip: " + str(total_cost) + " euros.")


get_trip_info()
