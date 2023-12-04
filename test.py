def input_data():
    while True:
        try:
            number = float(input('введите число: '))
            return number
        except ValueError as e:
            print(f'введено нечисловое значение')


def get_dict(dict_, key, value='по умолчанию'):
    try:
        return dict_[key]
    except KeyError as e:
        print('KeyError')
        return value

#print(input_data())
#dict_ = {1: 'one', 2: 'two'}
#print(get_dict(dict_=dict_, key=56))

