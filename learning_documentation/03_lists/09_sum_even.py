numbers = [3, 8, 12, 5, 20, 7, 14, 9]
total = 0
for number in numbers:
    if number % 2 == 0:
        total += number
print(total)