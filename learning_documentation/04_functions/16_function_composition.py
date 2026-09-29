#A code that uses 2 functions in one. 

def double(number):
    return number * 2

def double_and_add_one(number):
    result = double(number)
    return result + 1

print(double_and_add_one(7))