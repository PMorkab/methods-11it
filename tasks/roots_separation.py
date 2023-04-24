from misc import find_interval, bisection_method

def roots_separation_5():
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