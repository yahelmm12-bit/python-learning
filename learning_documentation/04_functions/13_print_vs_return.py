#Create two functions: The first one should use print to show the sum of two values. The second function will be using return to return the sum. After this, call the first function, store the result of the second function in a variable called result and finally print result.
def show_sum(a, b):
    print(a + b)

def get_sum(a, b):
    return a + b


show_sum(10, 5)

result = get_sum(10, 5)
print(result)