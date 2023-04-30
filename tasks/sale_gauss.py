import numpy as np

def gauss_method_8():
    #Ввод переменных

    # Запрос размера матрицы
    n = int(input("Введите размер матрицы: "))
    my_vars = input("Введите переменные через пробел: ").split()

    # Запрос матрицы системы уравнений
    print("Введите коэффициенты матрицы системы уравнений:")
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i][j] = eval(input("A[" + str(i + 1) + "][" + str(j + 1) + "]: "))

    # Запрос матрицы свободных членов
    print("\nВведите матрицу свободных членов:")
    B = np.zeros((n, 1))
    for i in range(n):
        B[i][0] = eval(input("B[" + str(i + 1) + "]: "))

    # Прямой ход
    for k in range(n - 1):
        for i in range(k + 1, n):
            coef = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= coef * A[k][j]
            B[i][0] -= coef * B[k][0]

    # Обратный ход
    x = np.zeros((n, 1))
    x[n - 1][0] = B[n - 1][0] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        sum_ = B[i][0]
        for j in range(i + 1, n):
            sum_ -= A[i][j] * x[j][0]
        x[i][0] = sum_ / A[i][i]

    # Вывод решения
    print("\nРешение системы уравнений:")
    for i in range(n):
        print(my_vars[i] + " = " + str(round(x[i][0], 2)))