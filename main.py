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

task = input("Выберите задачу:\n1. Абсолютная погрешность\n2. Относительная погрешность\n3. Математические операции\n4. Отделение корня уравнения\n5. Решение уравнения методом итераций или половинного деления\n")
# Обработка каждой задачи на основе пользовательского ввода
if task == '1':
    x1, x2 = map(float, input("Введите два числа через пробел: ").split())
    print(absolute_error(x1, x2))

    
elif task == '2':
    x1, x2 = map(float, input("Введите два числа через пробел: ").split())
    print(relative_error(x1, x2))
elif task == '3':
    n = int(input("Введите количество чисел: "))
    values = list(map(float, input(f"Введите {n} чисел через пробел: ").split()))
    least_decimal_places = find_least_precise(values)
    operation = None
    while operation not in operations:
        operation = input("Выберите операцию (1. Сложение, 2. Вычитание, 3. Умножение, 4. Деление): ")
    if operation in ('1', '2'):
        result = add_subtract(least_decimal_places, operations[operation], values)
    else:
        result = multiply_divide(least_decimal_places, operations[operation], values)
    print(result)
elif task == '4':
    coeffs = list(map(float, input("Введите коэффициенты через пробел: ").split()))  # Считываем коэффициенты
    powers = list(map(int, input("Введите степени x через пробел: ").split()))  # Считываем степени x

    print(f"Введенное уравнение: {equation_to_string(coeffs, powers)}")  # Выводим введенное уравнение

    # Находим производную и выводим ее на экран
    derivative_coeffs, derivative_powers = find_derivative(coeffs, powers)
    print(f"Производная уравнения: {equation_to_string(derivative_coeffs, derivative_powers)}")

    left, right = find_interval(coeffs, powers)  # Ищем интервал, содержащий один корень
    if left is None and right is None:
        print("На данном промежутке не найдено отделения корня.")
    else:
        f_derivative = lambda x: sum([coeff * x ** power for coeff, power in zip(derivative_coeffs, derivative_powers)])
        print(
            f"Значения производной на краях найденного промежутка: f'({left}) = {f_derivative(left)}; f'({right}) = {f_derivative(right)}")
        print(f"Отделение корня находится на промежутке [{left}, {right}]")
elif task == '5':
    degree = int(input("Введите наибольшую степень уравнения: "))
    coeffs = []
    for i in range(degree, -1, -1):
        coeff = float(input(f"Введите коэффициент перед x^{i}: "))
        coeffs.append(coeff)
    powers = list(range(degree, -1, -1))

    # Выполняем пункт 4 программы (уточнение корней)
    # ... (как и раньше)

    # Определяем функцию f, left и right
    f = lambda x: sum([coeff * x ** power for coeff, power in zip(coeffs, powers)])
    left, right = find_interval(coeffs, powers)

    # Запрос на ввод точности
    epsilon = float(input("Введите точность (например, 0.001): "))

    print("Выберите метод решения уравнения:")
    print("1. Метод итераций")
    print("2. Метод половинного деления")
    method_choice = input()

    if method_choice == '1':
        # Реализуйте метод итераций здесь
        pass
    elif method_choice == '2':
        root, tolerance = bisection_method(f, left, right, epsilon)
        print(f"x = {root} +- {tolerance}")
elif task == '6':
    degree = int(input("Введите наибольшую степень уравнения: "))
    coeffs = []
    for i in range(degree, -1, -1):
        coeff = float(input(f"Введите коэффициент перед x^{i}: "))
        coeffs.append(coeff)
    powers = list(range(degree, -1, -1))

    # Выполняем пункт 4 программы (уточнение корней)
    # ... (как и раньше)

    # Определяем функцию f, left и right
    f = lambda x: sum([coeff * x**power for coeff, power in zip(coeffs, powers)])
    left, right = find_interval(coeffs, powers)

    # Запрос на ввод точности
    epsilon = float(input("Введите точность (например, 0.001): "))

    root, tolerance = secant_method(f, left, right, epsilon)
    print(f"x = {root} +- {tolerance}")