from misc import relative_error

def relative_error_2():
    x1, x2 = map(float, input("Введите два числа через пробел: ").split())
    print(relative_error(x1, x2))