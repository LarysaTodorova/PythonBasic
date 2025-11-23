# Напишите функцию, которая проверяет на корректность адрес электронной почты,
# и возвращает
#    True, если адрес корректен, и False – если нет.
#    Функция имеет один параметр – адрес электронной почты. Представим,
#    что адрес корректен, если: он не менее 8 символов в длину, содержит «@»,
#    содержит точку и не содержит «#». Вызовите
#    функцию несколько раз, передав ей различные аргументы,
#    и выведите результаты в консоль.

def is_email_correct(email):
    is_length_correct = len(email) >= 8
    contains_at = "@" in email
    contains_dot = "." in email
    contains_hashtag = "#" in email
    result = is_length_correct and contains_at and contains_dot and not contains_hashtag
    return result


print(is_email_correct("test@test.com"))
print(is_email_correct("test@test.c#om"))
print(is_email_correct("t@t.com"))
print(is_email_correct("test.test.com"))
print(is_email_correct("test@testcom"))
