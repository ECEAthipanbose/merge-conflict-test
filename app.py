def greet(name):
    message = "Hello"
    return f"{message}, {name}!"

def calculate(a, b):
    result = a + b
    return result

if __name__ == "__main__":
    print(greet("World"))
    print(calculate(1, 2))
