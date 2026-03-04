def greet(name):
    message = "Hey"
    return f"{message}, {name}! Good to see you!"

def calculate(a, b):
    result = a * b
    return result

if __name__ == "__main__":
    print(greet("World"))
    print(calculate(1, 2))
