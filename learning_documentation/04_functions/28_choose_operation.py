def double(number):
    return number * 2

def triple(number):
    return number * 3

def choose_operation(operation_name):
    if operation_name == "triple":
        return triple
    elif operation_name == "double":
        return double
    else:
        print("Invalid operation name.")

operation = choose_operation("triple")

print(operation(10))