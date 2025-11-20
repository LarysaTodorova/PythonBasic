juice = int(input("Enter a juice volume(ml): "))
syrup = int(input("Enter a syrup volume(ml): "))
soda = int(input("Enter a soda volume(ml): "))

cocktailVolume = round((juice + syrup + soda) / 1000, 2)

print("Cocktail volume: ", cocktailVolume, "L")

