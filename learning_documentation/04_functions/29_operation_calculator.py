def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def choose_operation(operation_name):
    if operation_name == "add":
        return add
    elif operation_name == "subtract":
        return subtract
    elif operation_name == "multiply":
        return multiply

operation = choose_operation("multiply")
result = operation(6,7)
print(result)