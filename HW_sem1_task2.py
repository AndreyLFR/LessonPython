input_number = int(input('Введите число: '))
MIN_NUMBER = 0
MAX_NUMBER = 100
START_SIMPLICITY_TEST = 2

def simplicity_test(n):
    for i in range(START_SIMPLICITY_TEST, n):
        if n % i == 0:
            res = 'Составное'
            break
        else:
            res = 'Простое'
    return res

if input_number not in range(MIN_NUMBER, MAX_NUMBER+1):
    result = 'Сработало ограничение'
elif input_number == 0 or input_number == 1:
    result = 'И не простое, и не составное'
else:
    result = simplicity_test(n=input_number)
print(result)