from misc import absolute_error

def absolute_error_1():
    x1, x2 = map(float, input("Введите два числа через пробел: ").split())
    print(absolute_error(x1, x2))