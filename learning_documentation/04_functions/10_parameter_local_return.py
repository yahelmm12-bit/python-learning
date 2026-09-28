#Make a function called calculate_square that: Receives a number from within a parameter called number. Creates inside the functiona variable called result. Keeps inside result the square of the number. Return result. Outside the function, store the result in a variable. Print the result.
def calculate_square(number):
    result = number ** 2
    return result

print(calculate_square(7))