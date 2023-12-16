#Семинар 4 задача 2
import logging
import argparse


def key_params(**kwargs):
    logger.info('Запуск функции преобразования словаря')
    dict_ = {}
    logger.info('OK. Создан новый словарь')
    for key_, value_ in kwargs.items():
        if isinstance(value_, (list, dict, set, bytearray, type(None))):
            logger.info(f'Значение {value_} у ключа {key_} является нехешируемым')
            value_ = str(value_)
        dict_[value_] = key_
    logger.info('Функция завершилась')
    return dict_


logging.basicConfig(
    filename='log_task2.log',
    filemode='a',
    encoding='utf-8',
    format='{asctime} {levelname} {funcName} -> {lineno}: {msg}',
    style='{',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
argParser = argparse.ArgumentParser(description='Преобразование ключей и значений словаря')
argParser.add_argument('key_dict', metavar='k', help='введите ключи словаря через запятую без пробелов')
argParser.add_argument('value_dict', metavar='v', help='введите значения ключей словаря через запятую с соблюдением последовательности')
args = argParser.parse_args()
logger.info(f'Введены аргументы {args}')
if len(args.key_dict.split(',')) == len(args.value_dict.split(',')):
    logger.info('OK. Количество ключей и значений совпадает')
else:
    logger.error('Количество ключей и значений не совпадает')
    raise f'NegativeValueError: Количество ключей и значений не совпадает'
dict_ = {args.key_dict.split(',')[i]: args.value_dict.split(',')[i] for i in range(len(args.key_dict.split(',')))}

print(key_params(**dict_))