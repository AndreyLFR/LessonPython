number = int(input('Введите целое число: '))
result = ''
h = '0123456789ABCDEF'

print(hex(number))
while number > 0:
    result = h[number % 16] + result
    number = number // 16

print(f'0x{result}')