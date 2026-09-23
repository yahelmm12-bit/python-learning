numbers = [3, 8, 12, 5, 20, 7, 14, 9]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print (*even_numbers)
print (len(even_numbers))