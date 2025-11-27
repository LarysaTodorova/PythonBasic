def calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number == 0:
            return "You can't divide by 0"
        return first_number / second_number
    else:
        return "Invalid operation"


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
user_operation = input("Enter operation: ")

print(calculate(number1, number2, user_operation))
