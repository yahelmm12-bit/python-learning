def show_info(**argument):
    for key, value in argument.items():
        print(key, value)

show_info(name="Alex", age=14, country="Mexico")