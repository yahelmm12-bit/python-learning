def double(number):
    return number * 2

def triple(number):
    return number * 3

def apply_operation(number, operation):
    return operation(number)

print(apply_operation(10, double))
print(apply_operation(10, triple))