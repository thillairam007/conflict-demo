def validate_input(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number")
    return True

def format_result(result):
    return f"Result: {result}"
