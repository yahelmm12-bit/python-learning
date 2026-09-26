#Make a function called square that receives a number and returns its square. Then, save in result the square of 9. Multiply result by 2 and keep the result in double_result. Print double_result.

def square(number):
    return number ** 2

result = square(9)
double_result = result * 2
print(double_result)