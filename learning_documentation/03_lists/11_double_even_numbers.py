numbers = [3, 8, 12, 5, 20, 7, 14, 9]
for index in range((len(numbers))):
    if numbers[index] % 2 == 0:
        numbers[index] = numbers[index] * 2
print(numbers)


