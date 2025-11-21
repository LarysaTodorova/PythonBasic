def get_sum(number1, number2):
    summa = number1 + number2
    return summa


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print("First result: ", get_sum(first_number, second_number))
print("Second result: ", get_sum(first_number, first_number))
print("Third result: ", get_sum(second_number, second_number))