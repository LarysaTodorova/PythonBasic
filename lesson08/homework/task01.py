# Вам нужно перетащить тяжёлую мебель, помочь Вам может один из Ваших друзей - Петя или Вася.
# Напишите функцию, которая позволяет определить, сможете ли Вы перетащить мебель.
# Функция должна иметь два параметра – is_petya_free и is_vasya_free.
# Функция должна возвращать True, если мебель перетащить можно, и False – если нет.
# Мебель можно перетащить, если хотя бы один из друзей свободен.
# Создайте две переменные для каждого из друзей, содержащие значение, свободен ли Ваш друг.
# Вызовите функцию и выведите результат её работы на экран таким образом –
# «Получится ли перетащить мебель? – True/False».

def if_can_move_furniture(is_petya_free, is_vasya_free):
    return is_petya_free or is_vasya_free


petya_free = True
vasya_free = False

result = "Will it be possible to move the furniture? - " + str(if_can_move_furniture(petya_free, vasya_free))
print(result)