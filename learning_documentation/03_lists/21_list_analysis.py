#Make a program that: Prints the mayor withot using max(). Prints the lowest without using min(). Count how many numbers are even. Calculate the sum of all the numbers. And finally, that calculates the average.
numbers = [15, 4, 27, 8, 12, 31, 6, 20, 9]

counter_even = 0
total = 0

numbers.sort(reverse=True)
print(numbers[0])

numbers.sort()
print(numbers[0])

for number in numbers:
    if number % 2 == 0:
        counter_even += 1
print(counter_even)

for number in numbers:
    total += number
print(total)
print(total / len(numbers))
