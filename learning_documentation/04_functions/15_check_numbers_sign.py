#Create a function called check_number_sign(number). It should: Return "Positive" if the number is higher than 0; if it isn't, then return "Zero or negative". 

def check_number_sign(number):
    if number > 0:
        return "Positive"
    return "Zero or negative"

result = check_number_sign(10)
print(result)