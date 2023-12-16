import datetime
import logging

COUNT_DAY_WEEK = 7


def decorator_log(func):
    def wrapper(*args):
        logger.info(f'выполняется функция {args}')
        func(*args)
    return wrapper


@decorator_log
def reformat_data(str_date):
    dict_month = {'ноября': 11}
    dict_day_week = {'четверг': 4}
    list_date = str_date.split()
    month = dict_month[list_date[2]]
    day_week = dict_day_week[list_date[1]]
    number_day_week = int(list_date[0].split('-')[0])
    date_cur = datetime.date.today()
    year = date_cur.year
    for i in range(1, COUNT_DAY_WEEK+1):
        if datetime.date(year, month, i).isoweekday() == day_week:
            day = i + (COUNT_DAY_WEEK * number_day_week)
            break

    return datetime.date(year, month, day)

logging.basicConfig(
    filename='log.log',
    filemode='w',
    encoding='utf-8',
    format='{asctime} {levelname} {funcName} -> {lineno}: {msg}',
    style='{',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


reformat_data('2-й четверг ноября')