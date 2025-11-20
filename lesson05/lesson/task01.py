# storageLength = float(input("Enter a storage length: "))
# storageWidth = float(input("Enter a storage width: "))
# tableLength = float(input("Enter a table length: "))
# tableWidth = float(input("Enter a table width: "))
#
# storageArea = storageWidth * storageLength
# tableArea = tableWidth * tableLength
#
# tables = storageArea / tableArea
#
# print("Storage can accommodate ", tables, " tables.")

#///////////////////////////////////

# storageLength = float(input("Enter a storage length: "))
# storageWidth = float(input("Enter a storage width: "))
# tableLength = float(input("Enter a table length: "))
# tableWidth = float(input("Enter a table width: "))
#
# storageArea = storageWidth * storageLength
# tableArea = tableWidth * tableLength
#
# tables = storageArea // tableArea
#
# print("Storage can accommodate ", tables, " tables.")

#//////////////////////////////////////////////

storageLength = float(input("Enter a storage length: "))
storageWidth = float(input("Enter a storage width: "))
tableLength = float(input("Enter a table length: "))
tableWidth = float(input("Enter a table width: "))

storageArea = storageWidth * storageLength
tableArea = tableWidth * tableLength

tables = int(storageArea / tableArea)

print("Storage can accommodate ", tables, " tables.")

