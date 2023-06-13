# Программа проверяет является число положительным
# или отрицательным и выводит соответствующее событие.

num = 3

# Также попробуйте следующие варианты значения num.
# num = -5
# num = 0

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')


num_float = 3.4

# Также попробуйте варианты
# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


if num in [1, 2, 3, 4]:
    print('бакалавр')
if num in [5, 6]:
    print('магистр')
if num in [7, 8, 9]:
    print('аспирант')

if num > 100 or num < -100:
    print("-")
else:
    print('+')