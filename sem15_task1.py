#Напишите программу, которая использует модкль logging для вывода сообщений об ошибке в файл
#Отлавливаем ошибку деления на ноль

import logging

class Divide:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div(self):
        try:
            logger.info(f'все хорошо')
            c = self.a / self.b
        except ZeroDivisionError as e:
            logger.error(f'деление на ноль {e}')
            c = None
        return c


logging.basicConfig(
    filename='log.log',
    filemode='w',
    encoding='utf-8',
    format='{asctime} {levelname} {funcName} -> {lineno}: {msg}',
    style='{',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


obj1 = Divide(a=6, b=0)
print(obj1.div())