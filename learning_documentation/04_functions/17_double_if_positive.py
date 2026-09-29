#A function that checks if  the number is positive and doubles it. Else, it will return "Invalid number."

def double(number):
    return number * 2

def double_if_positive(number):
    if number > 0:
        result = double(number)
        return result
    else: 
        return "Invalid number"

print(double_if_positive(8))