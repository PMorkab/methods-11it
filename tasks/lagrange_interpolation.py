from misc import lagrange_interpolation

def lagrange_interpolation_1012():
    n = int(input('Введите количество точек в таблице значений: '))
    print('Введите значения x и y через пробел (одна точка на строку): ')
    x_table = []
    y_table = []
    for i in range(n):
        x, y = map(float, input().split())
        x_table.append(x)
        y_table.append(y)

    N = float(input('Введите значение N: '))
    result = lagrange_interpolation(x_table, y_table, n, N)

    print(f'Приближенное значение функции в точке {N} равно {result}')