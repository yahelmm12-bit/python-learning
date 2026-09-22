#Using for: Print all the numbers. Print only the numbers larger than 15. Count how many numbers are larger than 15. Calculate the sum of all the numbers. Calculate the sum of all the numbers larger than 15.
numbers = [12, 7, 25, 4, 18, 31, 10]

counter = 0
accumulator = 0
accumulator_2 = 0

for number in numbers:
    print(number)
    accumulator += number

    if number > 15:
        print(number)
        counter += 1
        accumulator_2 += number
print(counter)
print(accumulator)
print(accumulator_2)