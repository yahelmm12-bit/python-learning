numbers = [7, 25, 3, 18, 42, 11, 6, 30]
numbers.sort(reverse=True)
for number in numbers:
    if number > 10:
        print(number)