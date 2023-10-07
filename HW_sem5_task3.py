
def fibonacci(n=100000000):
    fib1 = 1
    for i in range(0, n):
        if i == 0 or i == 1:
            fib2 = i
        elif i == 2:
            fib2 == 1
        else:
            fib1, fib2 = fib2, fib1 + fib2
        yield fib2

f = fibonacci()

for i in range(10):
    print(next(f))