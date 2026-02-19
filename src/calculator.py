import logging
from src.utils import validate_input, format_result

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add(a, b):
    validate_input(a)
    validate_input(b)
    result = a + b
    logger.info(f"add({a}, {b}) = {result}")
    return format_result(result)

def subtract(a, b):
    validate_input(a)
    validate_input(b)
    result = a - b
    logger.info(f"subtract({a}, {b}) = {result}")
    return format_result(result)

def multiply(a, b):
    validate_input(a)
    validate_input(b)
    result = a * b
    logger.info(f"multiply({a}, {b}) = {result}")
    return format_result(result)

def main():
    print("Calculator v2.0 - with validation & logging")
    print(add(10, 5))

if __name__ == "__main__":
    main()