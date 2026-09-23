numbers = [17, 4, 29, 11, 35, 8, 22]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest += number
        largest = number
print(largest)
