#    Вы отправляетесь в путешествие по Европе, и у Вас есть 1000 у.е.
#    Напишите программу, которая должна выполнять следующие действия:
#    - задает два вопроса, сколько денег Вы потратили в Париже на шоппинг и экскурсии
#    - выводит на экран информацию, сколько денег осталось после Парижа
#    - задает два вопроса, сколько денег Вы потратили в Мадриде на экскурсии и рестораны
#    - выводит на экран информацию, сколько денег осталось после Мадрида
#    - задает два вопроса, сколько денег Вы потратили в Афинах на музеи и отель
#    - выводит на экран информацию, сколько денег осталось после Афин

money = 1000

parisShopping = float(input("How much money did you spend in Paris on shopping? "))
parisExcursions = float(input("How much money did you spend in Paris on excursions? "))
restAfterParis = money - parisShopping - parisExcursions
print("Rest after Paris: ", restAfterParis, " euro")

madridShopping = float(input("How much money did you spend in Madrid on shopping? "))
madridRestaurants = float(input("How much money did you spend in Madrid on restaurants? "))
restAfterMadrid = restAfterParis - madridShopping - madridRestaurants
print("Rest after Madrid: ", restAfterMadrid, " euro")

athensMuseums = float(input("How much money did you spend in Athens on museums? "))
athensHotels = float(input("How much money did you spend in Athens on hotels? "))
restAfterAthens = restAfterMadrid - athensMuseums - athensHotels
print("Rest after Athens: ", restAfterAthens, " euro")