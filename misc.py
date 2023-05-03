import math
import numpy as np

def menu():
    print('''    1.  Абсолютная погрешность
    2.  Относительная погрешность
    3.  Сумма и разность приближенных величин
    4.  Умножение и разность приближенных величин
    5.  Отделение корня уравнения
    6.  Решения уравнения методом деления корня пополам или методом итераций
    7.  Решение уравнения методом хорд
    8.  Решение СЛАУ методом Гаусса
    9.  Решение системы методом итераций/методом Зейделя
    10. Поиск приближенного значения функции в точкее по таблице значений
    11. Поиск приближенного значения функции в точке при отсутствии узла интерполяции в этой точке
    12. Поиск приближенного значения функции в точкее по таблице значений
    13. Экстраполирование Ньютона
    14. Решение дифференциального уравнения методом Эйлера или улучшенным
    15. Решение дифференциального уравнения методом Рунге-Кутта
    16. Поиск значения интеграла одним из методов Ньютона-Котеса
    17. Интегрирование по формулам Гаусса
    ''')

# Функция для расчета абсолютной погрешности
def absolute_error(x1, x2):
    return round(abs(x1 - x2),4)
# Функция для расчета относительной погрешности
def relative_error(x1, x2):
    return round(abs(x1 - x2) / max(abs(x1), abs(x2)),4)

def lagrange_interpolation(x, y, n, N):
    result = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (N - x[j]) / (x[i] - x[j])
            result += p * y[i]
        return result

def lagrange_extrapolation(x, y, n):
    def lagrange_basis(i):
        L = 1
        for j in range(n):
            if i != j:
                L *= (N - x[j]) / (x[i] - x[j])
        return L

    return sum(y[i] * lagrange_basis(i) for i in range(n))
# Функция проверки монотонности
def is_monotonic(f, A, B, step=0.1):
    sign = None
    x = A
    while x + step <= B:
        derivative = f(x + step) - f(x)
        if sign is None:
            sign = math.copysign(1, derivative)
        elif math.copysign(1, derivative) != sign:
            return False
        x += step

    return True

# Определяем функцию для вычисления значения многочлена Ньютона
def newton_poly(x, y):
    n = len(x)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            y[i] = (y[i] - y[i-1]) / (x[i] - x[i-j])
    return y

# Функция нахождения производной обобщенного уравнения
def find_derivative(coeffs, powers):
    derivative_coeffs = [coeff * power for coeff, power in zip(coeffs, powers)]
    derivative_powers = [power - 1 for power in powers]
    return derivative_coeffs, derivative_powers

# Функция выражения уравнения в виде строки
def equation_to_string(coeffs, powers):
    terms = [f"{coeff}x^{power}" if power > 0 else str(coeff) for coeff, power in zip(coeffs, powers)]
    return " + ".join(terms)

# Функция поиска интервала, содержащего один корень
def find_interval(coeffs, powers, step=0.1):
    f = lambda x: sum([coeff * x**power for coeff, power in zip(coeffs, powers)])  # Обобщенное уравнение
    x = -1000  # Начальное значение x

    while x < 1000:
        if f(x) * f(x + step) < 0 and is_monotonic(f, x, x + step, step):
            return x, x + step
        x += step

    return None, None
# Функция решения уравнения методом половинного деления
def bisection_method(f, left, right, epsilon):
    while abs(right - left) > 2 * epsilon:
        middle = left + (right - left) / 2
        if f(middle) * f(left) < 0:
            right = middle
        else:
            left = middle
    return left + (right - left) / 2, (right - left) / 2
# Функция решения уравнения методом Хорд
def secant_method(f, left, right, epsilon):
    x0, x1 = left, right
    while abs(x1 - x0) > epsilon:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x2
    return x1, abs(x1 - x0)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
# Функция для выполнения математических операций
operations = {'1': add, '2': subtract, '3': multiply, '4': divide}

def perform_operation(operation, values):
    result = values[0]
    for value in values[1:]:
        result = operation(result, value)
    return result

def round_to_pre_last_digit(value, least_decimal_places):
    value_str = format(value, f".{least_decimal_places + 1}f").rstrip('0').rstrip('.')
    return float(value_str[:-1])

def find_least_precise(values):
    least_decimal_places = float('inf')
    for value in values:
        decimal_places = len(str(value).split('.')[1])
        least_decimal_places = min(decimal_places, least_decimal_places)
    return least_decimal_places

def round_values(values, least_decimal_places):
    rounded_values = []
    for value in values:
        rounded_value = round(value, least_decimal_places + 1)
        rounded_values.append(rounded_value)
    return rounded_values

def add_subtract(least_decimal_places, operation, values):
    rounded_values = round_values(values, least_decimal_places)
    result = perform_operation(operation, rounded_values)
    return round_to_pre_last_digit(result, least_decimal_places)

def multiply_divide(least_decimal_places, operation, values):
    rounded_values = round_values(values, least_decimal_places)
    result = perform_operation(operation, rounded_values)
    return round(result, least_decimal_places)

# Решение дифференциального уравнения методом Эйлера
def euler(x0, y0, h, x_end):
    x = x0
    y = y0
    results = []
    while x < x_end:
        results.append((x, y))
        y = y + h * f(x, y)
        x = x + h
    results.append((x, y))
    return results

# Решение дифференциального уравнения методом Улучшенной схемы Эйлера
def improved_euler(x0, y0, h, x_end):
    x = x0
    y = y0
    results = []
    while x < x_end:
        results.append((x, y))
        y_pred = y + h * f(x, y)
        y = y + h/2 * (f(x, y) + f(x + h, y_pred))
        x = x + h
    results.append((x, y))
    return results

# Решение дифференциального уравнения методом Рунге-Кутта
def runge_kutta(x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
    return y

# Метод Гаусса с 2 узлами
def gauss_2(a, b, f):
    x1 = -1 / math.sqrt(3)
    x2 = 1 / math.sqrt(3)
    A1 = 1
    A2 = 1
    return ((b-a)/2) * (A1*f((b-a)/2 * x1 + (b+a)/2) + A2*f((b-a)/2 * x2 + (b+a)/2))

# Метод Гаусса с 3 узлами
def gauss_3(a, b, f):
    x1 = -math.sqrt(3/5)
    x2 = 0
    x3 = math.sqrt(3/5)
    A1 = 5/9
    A2 = 8/9
    A3 = 5/9
    return ((b-a)/2) * (A1*f((b-a)/2 * x1 + (b+a)/2) + A2*f((b-a)/2 * x2 + (b+a)/2) + A3*f((b-a)/2 * x3 + (b+a)/2))

# Метод Гаусса с 4 узлами
def gauss_4(a, b, f):
    x1 = -math.sqrt((3+2*math.sqrt(6/5))/7)
    x2 = -math.sqrt((3-2*math.sqrt(6/5))/7)
    x3 = math.sqrt((3-2*math.sqrt(6/5))/7)
    x4 = math.sqrt((3+2*math.sqrt(6/5))/7)
    A1 = (18-math.sqrt(30))/36
    A2 = (18+math.sqrt(30))/36
    A3 = A2
    A4 = A1
    return ((b-a)/2) * (A1*f((b-a)/2 * x1 + (b+a)/2) + A2*f((b-a)/2 * x2 + (b+a)/2) + A3*f((b-a)/2 * x3 + (b+a)/2) + A4*f((b-a)/2 * x4 + (b+a)/2))

def solve_system_iterative(a, b, epsilon, max_iterations):
    n = len(a)
    x = np.zeros(n)
    iterations = 0
    while iterations < max_iterations:
        new_x = np.zeros(n)
        for i in range(n):
            sum_ = 0
            for j in range(n):
                if j != i:
                    sum_ += a[i, j] * x[j]
            new_x[i] = (b[i] - sum_) / a[i, i]
        if np.linalg.norm(new_x - x) < epsilon:
            return new_x
        x = new_x
        iterations += 1
    print("Не удалось найти решение методом итераций.")


def solve_system_seidel(a, b, epsilon, max_iterations):
    n = len(a)
    x = np.zeros(n)
    iterations = 0
    while iterations < max_iterations:
        for i in range(n):
            sum_1 = sum(a[i, j] * x[j] for j in range(i))
            sum_2 = sum(a[i, j] * x[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum_1 - sum_2) / a[i, i]
        if np.linalg.norm(a @ x - b) < epsilon:
            return x
        iterations += 1
    print("Не удалось найти решение методом Зейделя.")
