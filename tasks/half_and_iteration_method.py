from misc import find_interval, secant_method

def half_and_iteration_6():
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

    root, tolerance = secant_method(f, left, right, epsilon)
    print(f"x = {root} +- {tolerance}")