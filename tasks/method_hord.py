from sympy import *

def hord_method_7():
    y = 0
    x = symbols('x')
    k = 0
    degree = int(input('Введите степень уравнения: '))
    print('Введите коэфицент от меньшего к большему:')
    for i in range(0, degree + 1):
        k = int(input())
        y += k * x ** i
    print("Ваши уравнения:" + str(y) + "=0")
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
        print('y=' + str(z) + ', при х=' + str(n))
        if za * z < 0:
            k += 1
            xlist.append(str(n))
            a = [n - 1, n]
            print('Корень уравнения' + str(a))
        za = zm
        zm = y.subs(x, -n)
        print('y=' + str(zm) + ', при x=' + str(-n))
        if za * zm < 0:
            k += 1
            xlist.append(str(-n + 1))
            a = [-n, -n + 1]
            print('корень' + str(a))
        n += 1
    print('Функция непрерывна')
    print('Проверим отрезки на монотонность')
    print('Производная равна: ' + str(diff(y, x)))
    xnull = solve(diff(y, x))
    print('Экстремумы 1 порядка равны ' + str(xnull))
    n = 0
    while (n < degree):
        i = 0
        xdel = False
        z = int(xlist[n])
        a = [z - 1, z]
        print('Проверим отрезок ' + str(a))
        while (i < degree - 1):
            zm = xnull[i]
            if zm > z or zm < z - 1:
                print('Функция монотонна на отрезке' + str(zm))
            else:
                print('Функция не монотонная')
                xdel = True
                break
            i += 1
        if not xdel:
            n += 1
    n = 0
    print('Корни оттделены')
    while (n < degree):
        z = int(xlist[n])
        a = [z - 1, z]
        print(str(a))
        n += 1
    print('Решить уравнение методом хорд ')
    t = 0.001
    n = 0
    while (n < degree):
        p = 1.0
        x3 = 0
        x2 = int(xlist[n])
        x1 = x2 - 1
        x4 = x1
        a = [x1, x2]
        print('Уточнение корня' + str(a))
        while (p > t):
            f1 = y.subs(x, x1)
            f2 = y.subs(x, x2)
            print('Вычислим х3 для следующихх значений:')
            print('x1=' + str(x1))
            print('x2=' + str(x2))
            print('f(x1)=' + str(f1))
            print('f(x2)=' + str(f2))
            print('Вычисляем...!')
            x3 = float(x1 - (((x2 - x1) * f1) / (f2 - f1)))
            print('x3=' + str(x3))
            p = abs(x4 - x3)
            print('Погрешность равна: ' + str(p))
            x4 = x3
            f3 = y.subs(x, x3)
            if (f1 * f3 < 0):
                x2 = x3
            else:
                x1 = x3
        print('---------')
        print('x=' + str(round(x3, 4)))
        print('---------')
        n += 1