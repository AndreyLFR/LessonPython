from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_NUMBER_ATTEMPTS = 10

desired_number = randint(LOWER_LIMIT, UPPER_LIMIT)

i = 1
result = 'Проиграл'
while i <= MAX_NUMBER_ATTEMPTS:
    user_answer = int(input('Введите число: '))
    if user_answer == desired_number:
        result = 'Угадал'
        break
    elif user_answer < desired_number:
        print(f'Больше. Осталось {MAX_NUMBER_ATTEMPTS - i} попыток')
    else:
        print('Меньше. Осталось {MAX_NUMBER_ATTEMPTS - i} попыток')
    i += 1
print(result)