#Your program should: Order the list from the smallest to the biggest numbers.
#Print the ordened list.
#Find and print the highest numberswithouth using max()
#Find and print the smallest number without using min()
#Count how many numbers are bigger than 10
#Calculate the sum of all the numbers.

total = 0
counter = 0
numbers = [12, 5, 18, 7, 20, 3, 15, 9, 22, 6]
numbers.sort(reverse=True)
print(numbers[0])
numbers.sort
print(numbers[0])
for number in numbers:
    if number > 10:
        counter += 1
print(counter)

for number in numbers:
    total += number 
print(total)