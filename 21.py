import logging

# configure the logging settings
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app2.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("arithematic_app")

def add(a,b):
    logger.debug(f"Adding {a} and {b}")
    return a+b

def subst(a,b):
    logger.debug(f"Subtracting {b} from {a}")
    return a-b

def multiply(a,b):
    logger.debug(f"Multiplying {a} and {b}")
    return a*b

def divide(a,b):
    logger.debug(f"Dividing {a} by {b}")
    try:
        result=a/b
    except ZeroDivisionError as e:
        logger.error("Division by zero error")
        return None
    return result


add(10,5)
subst(10,5)
multiply(10,5)
divide(10,0)
divide(10,2)