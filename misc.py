import math
# Функция для расчета абсолютной погрешности
def absolute_error(x1, x2):
    return round(abs(x1 - x2),4)
# Функция для расчета относительной погрешности
def relative_error(x1, x2):
    return round(abs(x1 - x2) / max(abs(x1), abs(x2)),4)


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
