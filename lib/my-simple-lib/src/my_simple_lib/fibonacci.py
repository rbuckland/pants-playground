def fibonacci1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n - 1) + fibonacci1(n - 2)

def fibonacci2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci3(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
