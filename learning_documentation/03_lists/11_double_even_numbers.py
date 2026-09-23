numbers = [3, 8, 12, 5, 20, 7, 14, 9]
for index in range((len(numbers))):
    if numbers[index] % 2 == 0:
        numbers[index] = numbers[index] * 2
print(numbers)

temperaturas = [-2, 5, 0, -8, 12, -4, 15]
for index in range(len(temperaturas)):
    if temperaturas[index] < 0:
        temperaturas[index] = 0
print(temperaturas)

