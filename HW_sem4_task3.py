import decimal

MULTIPLICITY = decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(5000)
RICHNESS_PERCENT = decimal.Decimal(0.05)
MIN_REMOVAL = decimal.Decimal(10)
MAX_REMOVAL = decimal.Decimal(100)
REMOVAL = decimal.Decimal(0.15)

balance = 0
operations = []

def check_multiplicity(amount):
    """
    проверка кратности суммы при пополнении и снятии
    :param amount:
    :return:
    """
    return True if amount % MULTIPLICITY == 0 else False


def deposit(amount):
    """
    пополнение счета
    :param amount:
    :return:
    """
    if check_multiplicity(amount=amount):
        global balance
        nalog = (amount * RICHNESS_PERCENT).quantize(decimal.Decimal(1)) if amount > RICHNESS_SUM else 0
        balance = balance + amount - nalog
        operations.append(f'Пополнение карты на {amount} у.е. Итого {balance} у.е.')


def withdraw(amount):
    """
    снятие денег
    :param amount:
    :return:
    """
    if check_multiplicity(amount=amount):
        global balance
        commission = MAX_REMOVAL.quantize(decimal.Decimal(1)) if amount * REMOVAL > MAX_REMOVAL else max(MIN_REMOVAL, amount * REMOVAL).quantize(decimal.Decimal(1))
        balance = balance - amount - commission
        operations.append(f'Снятие с карты True у.е. Процент за снятие {commission}. Итого {balance} у.е.')


def exit():
    global balance, operations
    if balance > RICHNESS_SUM:
        balance = decimal.Decimal(balance - balance * RICHNESS_PERCENT).quantize(decimal.Decimal(1))
    operations.append(f'Возьмите карту на которой {balance} у.е.')

deposit(6000)
withdraw(200)
exit()

print(operations)