#Given the list, ask the user for a number. Then, check if that number is in the list.
numbers = [12, 7, 25, 4, 18, 31, 10]
number = int(input("Enter a number: "))
if number in numbers:
    print(f"{number} was found.")
else:
    print(f"{number} was not found.")