# Напишите функцию, которая определяет, открыт ли офис.
# Функция должна возвращать True, если открыт, и False – если нет.
# Функция должна иметь три параметра – hours, is_weekend, is_holiday.
# Офис открыт в любой день, кроме выходных и праздников,
# если на часах время в диапазоне либо с 8 до 12 ч. включительно,
# либо с 14 до 18 ч. включительно (учитываем только часы, без минут).
# Вызовите функцию и выведите результат её работы на экран таким образом – «Офис открыт? – True/False».

def if_office_is_open(hours, is_weekend, is_holiday):
    morning = (8 <= hours) and (hours <= 12)
    evening = (14 <= hours) and (hours <= 18)
    # Офис открыт, если всё вместе True: НЕ выходной и НЕ праздник и (утреннее ИЛИ вечернее время)
    return (not is_weekend) and (not is_holiday) and (morning or evening)


current_hour = 10
weekend = True
holiday = True

result = "Is the office open? - " + str(if_office_is_open(current_hour, weekend, holiday))
print(result)
