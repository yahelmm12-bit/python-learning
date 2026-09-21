#A program that keeps asking the user for the correct password but with a maximun of only 3 attempts. 
#Probably the most important exercise today. I combined while loops, inputs, if/else, counter and break.
correct_password = "python123"
tries = 3
while tries > 0:
    entered_password = str(input("Please, enter the password: "))
    if entered_password == correct_password:
        print("Acces granted!")
        break
    else:
        tries -= 1
        if tries > 0:
            print(f"You still have {tries} try/tries left.")
        else:
            print("You have finished all your tries. Access blocked.")
