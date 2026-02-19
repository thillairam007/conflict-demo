from src.utils import validate_input, format_result

def add(a, b):
    validate_input(a)
    validate_input(b)
    result = a + b
    return format_result(result)

def subtract(a, b):
    validate_input(a)
    validate_input(b)
    result = a - b
    return format_result(result)

def multiply(a, b):
    validate_input(a)
    validate_input(b)
    result = a * b
    return format_result(result)

def main():
    print("Calculator v2.0 - with validation")
    print(add(10, 5))

if __name__ == "__main__":
    main()
