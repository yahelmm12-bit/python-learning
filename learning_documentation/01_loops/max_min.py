numbers = [15, 4, 22, 8, 31, 10, 27]
mayor = numbers[0]
for numero in numbers: 
    if numero > mayor:
        mayor = numero
print(mayor)

number_accumulator = 0
number_counter = 0
numbers = [3, 12, 7, 25, 18, 4, 30]
for number in numbers:
    if number > 10:
        number_accumulator += number
        number_counter += 1

numbers = [15, 4, 27, 8, 19, 2, 34, 11]
lowest = 100
for number in numbers:
    if number > 10:
        if lowest > number:
            lowest = number
print(lowest)

highest = 0
numbers = [4, 17, 9, 23, 12, 31, 6, 28]
for number in numbers:
    if number % 2 != 0:
        if number > highest:
            highest = number
print(highest)
