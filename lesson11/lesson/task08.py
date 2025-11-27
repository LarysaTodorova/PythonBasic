user_number = int(input("Enter a number: "))

value_to_insert = ""

if user_number % 2:
    value_to_insert = "not "

print("Your number is " + value_to_insert + "even")