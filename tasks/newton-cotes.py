# импортируем необходимые библиотеки
import numpy as np
from misc import newton_poly

# определяем подынтегральную функцию
def f(x):
    return np.sin(x) # здесь можно заменить на любую другую функцию


def newton_cotes():
    # задаем границы интегрирования
    a = float(input("Введите левую границу интегрирования: "))
    b = float(input("Введите правую границу интегрирования: "))

    # задаем количество разбиений на прямоугольники
    n = int(input("Введите количество разбиений: "))

    # выбираем метод Ньютона-Котеса
    print("Выберите метод Ньютона-Котеса:")
    print("1 - Метод прямоугольников")
    print("2 - Метод трапеций")
    print("3 - Метод Симпсона")
    print("4 - Метод интерполяции Ньютона-Котеса")
    choice = int(input())

    if choice == 1:
      # Метод прямоугольников
      # вычисляем ширину каждого прямоугольника
      h = (b-a)/n

      # создаем массив точек, на которых будем вычислять значение функции
      x = np.linspace(a, b, num=n+1)

      # вычисляем значение интеграла методом прямоугольников
      integral = h * np.sum(f(x))

    elif choice == 2:
      # Метод трапеций
      # вычисляем ширину каждого трапеции
      h = (b-a)/n

      # создаем массив точек, на которых будем вычислять значение функции
      x = np.linspace(a, b, num=n+1)

      # вычисляем значение интеграла методом трапеций
      integral = h/2 * (f(a) + 2*np.sum(f(x[1:-1])) + f(b))

    elif choice == 3:
      # Метод Симпсона
      # вычисляем ширину каждого интервала
      h = (b-a)/(2*n)

      # создаем массив точек, на которых будем вычислять значение функции
      x = np.linspace(a, b, num=2*n+1)

      # вычисляем значение многочлена Ньютона-Котеса в узлах интерполяции
      y = f(x)
      c = newton_poly(x, y)

      # вычисляем значение интеграла методом Симпсона
      integral = h/3 * np.sum(c[0::2] + 4*c[1::2] + c[2::2])

    elif choice == 4:
      # Метод интерполяции Ньютона-Котеса
      # вычисляем ширину каждого интервала
      h = (b-a)/n

      # создаем массив точек, на которых будем вычислять значение функции
      x = np.linspace(a, b, num=n+1)

      # вычисляем значение многочлена Ньютона-Котеса в узлах интерполяции
      y = f(x)
      c = newton_poly(x, y)

      # вычисляем значение интеграла методом интерполяции Ньютона-Котеса
      integral = (b-a)/n * np.sum(c)

    else:
      print("Неверный выбор метода.")
      exit()

    # выводим результат
    print("Значение интеграла:", integral)