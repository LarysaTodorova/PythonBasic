def can_we_by_groceries(is_lidl_open, is_kaufland_open):
    return is_lidl_open or is_kaufland_open


lidl = True
kaufland = False

groceries_bought = can_we_by_groceries(lidl, kaufland)
print("Can we buy groceries now? - " + str(groceries_bought))
