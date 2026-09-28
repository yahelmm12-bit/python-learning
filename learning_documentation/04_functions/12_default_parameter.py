#Make a function  called greet that: Receives a parameter called name. Has "programmer" as default value.  Prints Hello, {name}. Call it without and argument. Call it once more with "Alex."
def greet(name="programmer"):
    print(f"Hello, {name}!")

greet()
greet("Alex")