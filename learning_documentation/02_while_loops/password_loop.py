#A password program that repeatedly prompts the user until the correct password is entered.
correct_password = "python123"
entered_password = str(input("Please, enter the password: "))
while entered_password != correct_password:
    print("Invalid password. Please try again.")
    entered_password = (input("Please, enter the password: "))
print("Access granted!")
