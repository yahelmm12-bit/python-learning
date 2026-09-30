#Make a function using *args
def sum_all(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(sum_all(5, 10, 15))
print(sum_all(2, 4, 6, 8, 10))