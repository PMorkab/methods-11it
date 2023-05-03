from misc import lagrange_extrapolation
import numpy as np

def lagrange_extrapolation_11():
    n = int(input("Введите количество узлов: "))
    x = np.zeros(n)
    y = np.zeros(n)
    print("Введите значения (x_i, y_i):")
    for i in range(n):
        x[i], y[i] = map(float, input().split())
    N = float(input("Введите интересующую точку N: "))

    y_N = lagrange_extrapolation(x, y, n)
    print(f"Приближенное значение функции в точке N = {N} равняется {y_N}")