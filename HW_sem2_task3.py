import fractions

str_one = input('введите строку 1: ')
str_two = input('введите строку 2: ')

def disassemble(str, a=0, b=0):
    for i, element in enumerate(str):
        if element == '/':
            a = str[:i]
            b = str[i+1:]
    return [int(a), int(b)]

def _gcd(a, b):
    a, b = max(abs(a), abs(b)), min(abs(a), abs(b))
    while a % b != 0:
        a, b = b, a % b
    return b

a_sum = disassemble(str_one)[0] * disassemble(str_two)[1] + disassemble(str_one)[1] * disassemble(str_two)[0]
a_multiplication = disassemble(str_one)[0] * disassemble(str_two)[0]
b = disassemble(str_one)[1] * disassemble(str_two)[1]
sum_fraction = str(round(a_sum/_gcd(a_sum, b))) + '/' + str(round(b/_gcd(a_sum, b)))
multiplication_fraction = str(round(a_multiplication/_gcd(a_multiplication, b))) + '/' + str(round(b/_gcd(a_multiplication, b)))

print(sum_fraction, multiplication_fraction)

f_one = fractions.Fraction(str_one)
f_two = fractions.Fraction(str_two)
print(f_one + f_two, f_one * f_two)