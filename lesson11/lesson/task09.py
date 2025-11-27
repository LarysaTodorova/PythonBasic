def calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
user_operation = input("Enter operation: ")

print(calculate(number1, number2, user_operation))