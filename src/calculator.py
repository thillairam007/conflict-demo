import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add(a, b):
    result = a + b
    logger.info(f"add({a}, {b}) = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.info(f"subtract({a}, {b}) = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.info(f"multiply({a}, {b}) = {result}")
    return result

def main():
    print("Calculator v1.0 - with logging")
    print(add(10, 5))

if __name__ == "__main__":
    main()
