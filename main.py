from tasks.absolute_error import absolute_error_1
from tasks.relative_error import relative_error_2
from tasks.sum_or_difference import sum_or_difference_3
from tasks.product_or_private import product_or_private_4
from tasks.roots_separation import separate_roots_5
from tasks.half_and_iteration_method import half_and_iteration_6
from tasks.method_hord import hord_method_7
from tasks.sale_gauss import gauss_method_8
from tasks.iteration_or_seidel import iteration_or_seidel_9
from tasks.lagrange_interpolation import lagrange_interpolation_1012
from tasks.lagrange_extrapolation import lagrange_extrapolation_11
from tasks.euler_method import euler_method_14
from tasks.runge_kutta_method import runge_kutta_15
from tasks.newton_cotes import newton_cotes_16
from misc import menu

menu()

while True:
    task = input('Выберите задание: ')

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
    elif task == '10' or task == '12':
        lagrange_interpolation_1012()
    elif task == '11':
        lagrange_extrapolation_11()
    elif task == '14':
        euler_method_14()
    elif task == '15':
        runge_kutta_15()
    elif task == '16':
        newton_cotes_16()
    elif task == 'menu':
        menu()
