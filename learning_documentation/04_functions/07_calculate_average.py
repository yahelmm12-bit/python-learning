#Create a function called "calculate_average" that receives a list of numbers. The function should: Create an accumulator, go trough the list using for. Sum all the numbers. Calculate the average using len(). Return the average using return.

list_of_numbers = [10, 20, 30, 40, 50]
def calculate_average(numbers):
    accumulator = 0
    for number in numbers:
        accumulator += number
    average = accumulator / len(numbers)
    return average

result = calculate_average(list_of_numbers)
print (result)