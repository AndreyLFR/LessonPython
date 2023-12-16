#Семинар 6 задача 1 'Проверка корректности даты'
import logging
import argparse

def check_date(str):
    res = False
    day, mounth, year = str.split('.')
    for i in [day, mounth, year]:
        try:
            int(day)
            logger.info(f'OK. {i} имеет корректный формат')
        except ValueError as e:
            logger.error(f'{i} должен быть числом')
            raise f'{i} должен быть числом {e}'
    date_dict = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30}
    date_dict[2] = 29 if int(year) % 4 == 0 else 28
    if int(mounth) in date_dict.keys() and 0 < int(day) < date_dict.get(int(mounth), 0):
        res = True
    logger.info(f'Функция завершилась c результатом {res}')
    return res

logging.basicConfig(
    filename='log_task3.log',
    filemode='a',
    encoding='utf-8',
    format='{asctime} {levelname} {funcName} -> {lineno}: {msg}',
    style='{',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
argParser = argparse.ArgumentParser(description='Проверка корректности даты')
argParser.add_argument('input_date', metavar='d', help='введитуе дату в формате DD.MM.YYYY')
args = argParser.parse_args()
logger.info(f'Введены аргументы {args}')

print(check_date(args.input_date))