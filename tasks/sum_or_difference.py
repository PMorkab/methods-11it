from misc import find_least_precise, operations, add_subtract, multiply_divide

def sum_or_difference_3():
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