#Print all the numbers in this list
#Print only the first element
#Print the last element
# Change 30 for 35
# Add 60 at the end
# Print the resulting list 
#Print how many elements this list have
counter = 0
numbers = [10, 20, 30, 40, 50]
print(*numbers)
print(numbers[0])
print(numbers[4])
numbers[2] = 35
print(numbers[2])
numbers.insert(5, 60)
print(numbers[5])
print(*numbers)
for number in (numbers):
    counter += 1
print(counter)