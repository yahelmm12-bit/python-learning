def show_data(*numbers, **information):
    total = 0
    for number in numbers:
        total += number
    print(total)

    for key, value in information.items():
        print(key,value)

show_data(10, 20, 30, name="Alex", country="Mexico")