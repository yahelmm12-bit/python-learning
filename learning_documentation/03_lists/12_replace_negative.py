numbers = [4, -2, 7, -5, 10, -3, 8]

for number in range(len(numbers)):
    if numbers[number] < 0:
        numbers[number] = 0
print(numbers)