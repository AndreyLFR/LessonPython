def data_input(name_side):
    return int(input(f'Введите длину стороны {name_side}: '))

def length_check(a, b, c):
    if a == b and a == c:
        res = 'Равносторонний'
    elif a == b or b == c or a == c:
        res = 'Равнобедренный'
    else:
        res = 'Разносторонний'
    return res

a = data_input('a')
b = data_input('b')
c = data_input('c')
result = 'Не существует' if a + b < c or a + c < b or b + c < a else length_check(a=a, b=b, c=c)

print(result)