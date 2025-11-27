correct_password = "qwerty"

user_password = input("Enter your password: ")

if user_password == correct_password:
    print("Successful login")
else:
    print("Access denied! Incorrect password!")
