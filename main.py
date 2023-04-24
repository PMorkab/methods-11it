from tasks.absolute_error import absolute_error_1
from tasks.relative_error import relative_error_2
from tasks.sum_or_difference import sum_or_difference_3
from tasks.product_or_private import product_or_private_4
from tasks.roots_separation import roots_separation_5
from tasks.half_and_iteration_method import half_and_iteration_6

task = input('''1. Абсолютная погрешность
2. Относительная погрешность
3. Математические операции
4. Отделение корня уравнения
5. Решение уравнения методом итераций или половинного деленияы
6. Решения уравнения методом деления корня пополам или методом итераций
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
    roots_separation_5()
elif task == '6':
    half_and_iteration_6()