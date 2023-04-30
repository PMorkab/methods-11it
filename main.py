from tasks.absolute_error import absolute_error_1
from tasks.relative_error import relative_error_2
from tasks.sum_or_difference import sum_or_difference_3
from tasks.product_or_private import product_or_private_4
from tasks.roots_separation import separate_roots_5
from tasks.half_and_iteration_method import half_and_iteration_6
from tasks.method_hord import hord_method_7
from tasks.sale_gauss import gauss_method_8
from tasks.iteration_or_seidel import iteration_or_seidel_9
from tasks.euler_method import euler_method_14
from tasks.runge_kutta_method import runge_kutta_15
from tasks.newton_cotes import newton_cotes_16
from tasks.gaussian_integration import gaussian_integration_17

task = input('''1. Абсолютная погрешность
2. Относительная погрешность
3. Сумма и разность приближенных величин
4. Умножение и разность приближенных величин
5. Отделение корня уравнения
6. Решения уравнения методом деления корня пополам или методом итераций
7. Решение уравнения методом хорд
8. Решение СЛАУ методом Гаусса
9. Решение системы методом итераций/методом Зейделя
10. Интерполирование Лагранжа
11. Экстраполирование Ларгранжа
12. Интерполирование Ньютона
13. Экстраполирование Ньютона
14. Решение дифференциального уравнения методом Эйлера или улучшенным
15. Решение дифференциального уравнения методом Рунге-Кутта
16. Поиск значения интеграла одним из методов Ньютона-Котеса
17. Интегрирование по формулам Гаусса

Выберите задание: ''')

# Обработка каждой задачи на основе пользовательского ввода
if task == '1':
    absolute_error_1()
elif task == '2':
    relative_error_2()
elif task == '3':
    sum_or_difference_3()
elif task == '4':
    product_or_private_4()
elif task == '5':
    separate_roots_5()
elif task == '6':
    half_and_iteration_6()
elif task == '7':
    hord_method_7()
elif task == '8':
    gauss_method_8()
elif task == '9':
    iteration_or_seidel_9()
elif task == '14':
    euler_method_14()
elif task == '15':
    runge_kutta_15()
elif task == '16':
    newton_cotes_16()
elif task == '17':
    gaussian_integration_17()
