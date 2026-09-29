#Make a function called check_age that receives age. It should: Return "Minor" if age < 18 and if age >= 18 it should return "adult". Afterwards, store the result of check_age(14) in a variable. Finally, print that variable.

def check_age(age):
    if age < 18:
        return "You're a minor."
    else:
        return "You're an adult."

check = check_age(14)
print(check)
