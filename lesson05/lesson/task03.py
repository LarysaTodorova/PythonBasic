juice = int(input("Enter a juice volume(ml): "))
syrup = int(input("Enter a syrup volume(ml): "))
soda = int(input("Enter a soda volume(ml): "))

cocktailVolumeMl = juice + syrup + soda

cocktailVolumeLitre = cocktailVolumeMl / 1000

cocktailVolumeRounded = round(cocktailVolumeLitre, 2)

print("Cocktail volume: ", cocktailVolumeRounded, "L")

