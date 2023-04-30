import numpy as np
from misc import solve_system_iterative, solve_system_seidel

def iteration_or_seidel_9():
    # считываем размерность системы уравнений
    n = int(input("Введите размерность системы уравнений: "))

    # считываем коэффициенты системы уравнений
    a = np.zeros((n, n))
    b = np.zeros(n)
    for i in range(n):
        row = input(f"Введите коэффициенты {i + 1} строки через пробел: ")
        row_values = row.split()
        for j in range(n):
            a[i, j] = float(row_values[j])
        b[i] = float(row_values[-1])

    # выбираем метод решения системы уравнений
    method = input("Выберите метод решения системы уравнений (И - итерации / З - Зейделя): ")
    if method.lower() == "и":
        epsilon = float(input("Введите желаемую точность решения: "))
        max_iterations = int(input("Введите максимальное число итераций: "))
        x = solve_system_iterative(a, b, epsilon, max_iterations)
        if x is not None:
            print("Решение системы уравнений методом итераций:")
            print(x)
    elif method.lower() == "з":
        epsilon = float(input("Введите желаемую точность решения: "))
        max_iterations = int(input("Введите максимальное число итераций: "))
        x = solve_system_seidel(a, b, epsilon, max_iterations)
        if x is not None:
            print("Решение системы уравнений методом Зейделя:")
            print(x)
    else:
        print("Некорректный метод решения системы уравнений.")