#База - семинар 3 задача 1
#Задание: добавить логирование, запуск из командной строки
import logging
import argparse

#items = {'ключи': 0.3,
#         'кошелек': 0.2,
#         'телефон': 0.5,
#         'зажигалка': 0.1,
#         }
#max_weight = 1.0

def packing_backpack(items, max_weight):
    logger.info('Запуск функции сбора рюкзака')
    try:
        max_weight = float(max_weight)
        logger.info('OK. Проверка максимального веса рюкзака')
    except ValueError:
        logger.error('В качестве максимального веса рюкзака введено значение типа не float или int. '
                     'Использовано значение по умолчанию 1.0')
        max_weight = 1.0
    try:
        items.items()
        logger.info('OK. Проверка перечня вещей')
    except TypeError:
        logger.error('Перечень вещей должен быть передан как словарь предмет: вес'
                     'В качестве дефолтного значения использован пустой перечень вещей')
        items = {}
    backpack = {}
    logger.info('OK. Создан пустой рюкзак')
    for item, weight in items.items():
        logger.info('ОК. Запустился цикл перебора перечня вещей')
        logger.info('ОК. Проверка наименования вещей') if isinstance(item, str) else logger.warning('Вещь заведена не в строковом формате. Необходима проверка')
        try:
            weight = float(weight)
            logger.info(f'OK. Проверка веса вещи {item}')
        except ValueError as e:
            logger.error(f'вес вещи {item} не число')
            raise f'NegativeValueError: {e}'

        if weight <= max_weight:
            backpack[item] = weight
            max_weight -= weight
    return backpack


logging.basicConfig(
    filename='log.log',
    filemode='a',
    encoding='utf-8',
    format='{asctime} {levelname} {funcName} -> {lineno}: {msg}',
    style='{',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

argParser = argparse.ArgumentParser(description='Программа по сбору рюкзака')
argParser.add_argument('max_weight', metavar='wm', help='максимальный вес рюкзака')
argParser.add_argument('items', metavar='i', help='перечень вещей через запятую без пробелов')
argParser.add_argument('weight', metavar='wi', help='веса вещей через запятую без пробелов')
args = argParser.parse_args()
logger.info(f'Введены аргументы {args}')
if len(args.items.split(',')) == len(args.weight.split(',')):
    logger.info('OK. Количество значений наименований вещей и весов совпадает')
else:
    logger.error('Количество вещей и их весов не совпадает')
    raise f'NegativeValueError: Количество вещей и их весов не совпадает'
items = {args.items.split(',')[i]: args.weight.split(',')[i] for i in range(len(args.items.split(',')))}
print(packing_backpack(items=items, max_weight=args.max_weight))