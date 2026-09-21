#A slightly more complex program than my previous ones. 
#This program constantly asks for a number until it is 0. At the end the program displays the sum of all the numbers entered and how many numbers were entered.
accumulator = 0
counter = 0
while True:
    number = int(input("Please write a number: "))
    if number == 0:
        break
    accumulator += number
    counter += 1
print(f"Sum: {accumulator}")
print(f"Numbers entered: {counter}")

