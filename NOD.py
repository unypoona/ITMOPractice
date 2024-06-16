'''5.def_while_НОД_Задание'''
""" 1. Подсчет количества итераций 
k = 0   # глобальная переменная
def Countgit_1(n):
    ''' Функция как процедура, изменяющая глобальную переменную'''
    global k
    while n > 0:    # прекратить действия, когда n станет 0
        n = n//10   # Отбрасывание последней цифры числа n
        k = k + 1   # Увеличение значения переменной-счетчика

test_num = 1234568
Countgit_1(test_num) # вызов процедуры
print("Количество цифр в числе", k)  # вывод результата


def Countgit_2(n):
    ''' Функция, возвращающая значение'''
    k = 0   # локальная переменная
    while n > 0:    # прекратить действия, когда n станет 0
        n = n//10   # Отбрасывание последней цифры числа n
        k = k + 1   # Увеличение значения переменной-счетчика
    return k

test_num = 1234568

h = Countgit_2(test_num)
print("Количество цифр в числе", h)
"""


''' Задание. Требуется реализовать алгоритм Евклида как функцию -
вариант на свое усмотрение
2. Алгоритм Евклида 

a = int(input('Задайте первое число '))
b = int(input('Задайте второе число '))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
nod = a

print('НОД равен', nod)
'''
def nod_rec(a, b):
    #через рекурсию
    if b == 0:
        return a
    else:
        return nod_rec(b, a % b)

# Ввод чисел
a = int(input('Задайте первое число: '))
b = int(input('Задайте второе число: '))

# Вычисление НОД с использованием рекурсии
nod = nod_rec(a, b)
print('НОД равен', nod)