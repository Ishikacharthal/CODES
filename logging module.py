
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("AdvancedLogger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = RotatingFileHandler(
    "application.log",
    maxBytes=1024,
    backupCount=3
)
file_handler.setLevel(logging.DEBUG)


formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def divide(a, b):
    try:
        result = a / b
        logger.info("Division performed successfully")
        return result

    except ZeroDivisionError:
        logger.error("Cannot divide by zero!")
        return None

def main():
    logger.debug("Application started")
    logger.info("Program is running")
    logger.warning("This is a warning message")

    result = divide(20, 5)
    print("Result:", result)

    divide(10, 0)

    try:
        number = int("Python")
    except ValueError:
        logger.exception("Invalid conversion occurred")

    logger.critical("Critical message example")
    logger.info("Application finished")

if __name__ == "__main__":
    main()
