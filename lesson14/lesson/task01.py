list_1 = []
list_2 = []

print(list_1)

list_1.append(12)
list_1.append(13)
list_1.append(7)

list_2.append(5)

number = 15
list_2.append(number)

print(list_1)
print(list_2)

list_1[1] = 9
list_2[0] = 3
print(list_1)
print(list_2)
print(list_1[2])

list_length = len(list_1)
print("Size list 1: ", list_length)
print("Size list 2: ", len(list_2))

list_1.append(20)
print(list_1)
print("Size list 1: ", len(list_1))

