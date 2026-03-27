from logger import info

def greet(name):
    message = "Hello"
    info(f"Greeting {name}")
    return f"{message}, {name}! Welcome!"

def calculate(a, b, op="add"):
    if op == "add":
        result = a + b
    elif op == "multiply":
        result = a * b
    else:
        raise ValueError(f"Unknown op: {op}")
    return result

if __name__ == "__main__":
    print(greet("World"))
    print(calculate(1, 2))
    print(calculate(3, 4, op="multiply"))
