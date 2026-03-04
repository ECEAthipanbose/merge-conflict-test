def greet(name):
    message = "Hi there"
    return f"{message}, {name}! Welcome!"

def calculate(a, b):
    result = a - b
    return result

if __name__ == "__main__":
    print(greet("World"))
    print(calculate(1, 2))
