import logging

logging.basicConfig(
        filename='log.log',
        filemode='w',
        encoding='utf-8',
        format='{asctime} {levelname} {funcName} -> {lineno}: {msg}',
        style='{',
        level=logging.INFO
    )
logger = logging.getLogger(__name__)

def decorator_log(func):
    def wrapper(*args):
        logger.info(f'выполняется функция {args}')
        func(*args)
    return wrapper

@decorator_log
def test_func(a=0, b=0):
    return a + b


test_func(3, 5)