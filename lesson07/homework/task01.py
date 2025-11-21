# Напишите программу, которая хранит в переменных данные, какой сейчас по счёту день в году (например, 48),
# и название следующего года (например, "Год Тигра").
# Программа должна посчитать, сколько дней осталось до следующего года и вывести на экран фразу по образцу -
# "Через 123 дня наступит Год Тигра". Для упрощения считайте, что в году всегда 365 дней.
# Оформите расчёт остатка количества дней до конца года в виде отдельной функции.
# Также в программе должна быть вторая функция,
# куда Вы передаёте количество оставшихся дней и название года, а она выводит требуемую строку на экран.

def calculate_remaining_days(today):
    remaining_days = 365 - today
    return remaining_days


def print_string(remaining_days, year_name):
    print("In " + str(remaining_days) + " the " + year_name + " will begin.")


day_of_the_year = 48
next_year_name = "Year of the Tiger"

number_of_days = calculate_remaining_days(day_of_the_year)
print_string(number_of_days, next_year_name)
