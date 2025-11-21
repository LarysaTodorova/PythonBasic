# Исходные данные: клиента банка зовут Аркадий,
# на его банковском счёте лежат 3000 у.е.
#    Напишите программу для приветственного окна банкомата,
#    которая выводит на экран фразу «Добрый день, Аркадий!» и на
#    следующей строке – «На Вашем счёте – 3000 у.е.».
#    В программе должны быть отдельная функция,
#    которая формирует и возвращает первую
#    строку, а также отдельная функция,
#    которая формирует и возвращает вторую строку.
#    Должна быть третья функция, которая, пользуясь
#    первыми двумя, выводит на экран обе строки
#    (функции в своём теле могут вызывать другие функции).

# def print_hallow(name):
#     print("Hallow, " + name + " !")
#
#
# def print_sum(summa):
#     print("On your account " + str(summa) + " euros.")
#
#
# def greeting(name, summa):
#     print_hallow(name)
#     print_sum(summa)
#
#
# user_name = "Arcadiy"
# user_summa = 3000
#
# greeting(user_name, user_summa)


def get_greeting(name):
    greeting = "Добрый день, " + name + "!"
    return greeting


def get_account_info(money_amount):
    info = "На Вашем счёте - " + str(money_amount) + " у.е."
    return info


def print_info(name, money_amount):
    string_1 = get_greeting(name)
    string_2 = get_account_info(money_amount)
    print(string_1)
    print(string_2)


name = "Аркадий"
money = 3000

print_info(name, money)
