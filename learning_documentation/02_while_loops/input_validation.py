#A program that asks the user for a positive number and doesn't stop until the user inputs a valid number.
number = int(input("Enter a positive number: "))

while number <= 0:
    print("Invalid number.")
    number = int(input("Enter a positive number: "))

print("Valid number!")
