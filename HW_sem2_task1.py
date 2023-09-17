INTEREST_WITHDRAWAL = 0.015
INTEREST_TAX = 0.1
TAX_CONTROL = 5_000_000
MIN_COMMISSION = 50
MAX_COMMISSION = 600
BANKNOTE_DENOM = 50

BONUS = 0.03
BONUS_COUNT = 3
balance = 0
counter = 0

def commission_calculation(transaction_amount):
    comission = INTEREST_WITHDRAWAL * transaction_amount
    if comission > MAX_COMMISSION: comission = MAX_COMMISSION
    elif comission < MIN_COMMISSION: comission = MIN_COMMISSION
    return comission

def tax(balance, interest_tax, tax_control_amount):
    if balance > tax_control_amount:
        print(f'___Сняли налог {interest_tax * 100}% с баланса в размере: {round(balance * interest_tax)}')
        balance = round((1 - interest_tax) * balance)
        print(f'___Остаток средств на счете: {balance}')
    return balance

def get_amount(balance):
    verified = False
    while not verified:
        balance = tax(balance=balance, interest_tax=INTEREST_TAX, tax_control_amount=TAX_CONTROL)
        amount = input('Введите сумму операции: ')
        if amount.isnumeric():
            verified = True if int(amount) % BANKNOTE_DENOM == 0 else print(f'Ошибка: введена сумма некратная {BANKNOTE_DENOM}')
        else:
            print('___Ошибка: введите число цифрами')
    return amount, balance

while True:
    act = input('1 - пополнить\n2 - снять\nлюбую другую, чтобы выйти\n')
    commission = 0
    if not act.isnumeric() or (int(act) != 1 and int(act) != 2):
        print(f'___Введена недопустимая операция. Работа завершена. Остаток средств на счете: {balance}')
        break
    else:
        counter += 1
        amount, balance = get_amount(balance)
        if int(act) == 1:
            balance = balance + int(amount)
        elif int(act) == 2:
            commission = commission_calculation(transaction_amount=int(amount))
            if (balance - int(amount) - commission) >= 0:
                balance = (balance - int(amount) - commission)
                print(f'___Комиссия за снятие денег {commission}')
            else: print('Нельзя снять больше, чем на счете')
        if counter % BONUS_COUNT == 0:
            print('___Начислен бонус')
            balance = round(balance * (1 + BONUS))

        print(f'___Остаток средств на счете: {balance}.')
