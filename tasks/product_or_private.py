from misc import equation_to_string, find_derivative, find_interval

def product_or_private_4():
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
        print(f"Значения производной на краях найденного промежутка: f'({left}) = {f_derivative(left)}; f'({right}) = {f_derivative(right)}")
        print(f"Отделение корня находится на промежутке [{left}, {right}]")