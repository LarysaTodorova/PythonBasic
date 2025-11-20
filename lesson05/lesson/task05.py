eurToDolRate = 1.09
moneyDol = 1000
depositInterest = 5
years = 3

moneyTotal = moneyDol * (1 + depositInterest / 100) ** years
incomeDol = moneyTotal - moneyDol
incomeEuro = incomeDol / eurToDolRate

print(incomeDol)
print(incomeEuro)
