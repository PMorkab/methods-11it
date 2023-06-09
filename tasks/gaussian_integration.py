from misc import gauss_2, gauss_3, gauss_4

def gaussian_integration_17():
    # Запрос границ интегрирования
    a = float(input("Введите нижнюю границу интегрирования: "))
    b = float(input("Введите верхнюю границу интегрирования: "))

    # Запрос функции
    func = input("Введите интегрируемую функцию: ")
    f = lambda x: eval(func)

    # Рассчет интеграла
    I_2 = gauss_2(a, b, f)
    I_3 = gauss_3(a, b, f)
    I_4 = gauss_4(a, b, f)

    # Вывод результата
    print("Интеграл методом Гаусса с 2 узлами: ", I_2)
    print("Интеграл методом Гаусса с 3 узлами: ", I_3)
    print("Интеграл методом Гаусса с 4 узлами: ", I_4)