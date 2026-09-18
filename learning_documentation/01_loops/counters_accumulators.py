number_counter = 0
for number in range (1, 31):
    if number % 4 == 0:
        number_counter += 1
print(number_counter)

number_counter = 0
for number in range (1,31):
    if number % 4 == 0:
        number_counter += number
print(number_counter)

number_total = 0
for number in range (1,51):
    if number % 2 == 0:
        number_total += number
print(number_total)

number_counter = 0
for number in range(1,101):
    if number % 2 == 0:
        number_counter += 1
print(number_counter)

number_accumulator = 0
for number in range(1,51):
    if number % 2 != 0:
        number_accumulator += number

number_accumulator = 0
number_counter = 0
numbers = [3, 12, 7, 25, 18, 4, 30]
for number in numbers:
    if number > 10:
        number_accumulator += number
        number_counter += 1
        
average = number_accumulator / number_counter
print(average)

numbers = [5, 12, 7, 20, 3, 18, 25, 10]
number_counter = 0
number_accumulator = 0
for number in numbers:
    if number > 10:
        number_counter += 1
        number_accumulator += number
average = number_accumulator / number_counter
print(average)
