for number in range(1, 21):
    if number % 3 == 0:
        print(number)

for number in range(1, 31):
    if number % 4 == 0:
        print(number)

number_total = 0
for number in range (1,51):
    if number % 2 == 0:
        number_total += number
print(number_total)
