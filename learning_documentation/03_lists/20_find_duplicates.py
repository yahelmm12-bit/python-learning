#Mae a program that prints the numbers that appears more than twice in the given list.
numbers = [4, 7, 2, 4, 9, 7, 1, 2, 8]
duplicates = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)
print(duplicates)