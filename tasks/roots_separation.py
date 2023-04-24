from sympy import symbols, diff, solve

def separate_roots_5():
    y = 0
    x = symbols('x')
    k = 0
    degree = int(input('Введите степень уравнения: '))
    print('Введите коэфицент от меньшего к большему:')
    for i in range(0, degree + 1):
        k = int(input())
        y += k * x ** i
    print(f"Ваше уравнение: {str(y)} = 0")
    print("Отделим корни уравнения")
    print("Построим таблицу значений")
    k = 0
    n = 0
    z = 0
    za = 0
    zm = 0
    xlist = list()
    while (k < degree):
        za = z
        z = y.subs(x, n)
        print(f'y = {str(z)}, при x = {str(n)}')
        if za * z < 0:
            k += 1
            xlist.append(str(n))
            a = [n - 1, n]
            print(f'Корень уравнения: {str(a)}')
        za = zm
        zm = y.subs(x, -n)
        print(f'y = {str(zm)}, при x = {str(-n)}')
        if za * zm < 0:
            k += 1
            xlist.append(str(-n + 1))
            a = [-n, -n + 1]
            print(f'корень {str(a)}')
        n += 1
    print('Функция непрерывна')
    print('Проверим отрезки на монотонность')
    print(f'Производная равна: {str(diff(y, x))}')
    xnull = solve(diff(y, x))
    print(f'Экстремумы 1 порядка равны {str(xnull)}')
    n = 0
    while (n < degree):
        i = 0
        xdel = False
        z = int(xlist[n])
        a = [z - 1, z]
        print(f'Проверим отрезок {str(a)}')
        while (i < degree - 1):
            zm = xnull[i]
            if zm > z or zm < z - 1:
                print(f'Функция монотонна на отрезке {str(zm)}')
            else:
                print('Функция не монотонная')
                xdel = True
                break
            i += 1
        if not xdel:
            n += 1
    n = 0
    print('Корни отделены')
    while (n < degree):
        z = int(xlist[n])
        a = [z - 1, z]
        print(str(a))
        n += 1
