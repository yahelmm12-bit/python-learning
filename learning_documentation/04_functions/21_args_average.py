#Make a function without a determined number of variables that calculates the average.

def calculate_average(*arg):
    total = 0
    for number in arg:
        total += number

    counter = len(arg)
    return total / counter

print(calculate_average(1, 3, 4, 5 ,6))