import datetime
#Как проверить високосный ли год?
'''
Стандартный год состоит из 365 дней, а високосный из 366 дней.

Правила определения:
Високосный год кратен 4, но при этом не кратен 100, либо кратен 400.
Иными словами, если год делится на 4 без остатка, но делится на 100 только с остатком,
то он високосный, иначе — невисокосный, кроме случая, если он делится без остатка на 400 — тогда он всё равно високосный.
'''
current_date = datetime.date.today()

year = current_date.year
#year = 1981
#year = 2025
'''Задание 1. Проверка с условиями if-else'''

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} является високосным годом.")
        else:
            print(f"{year} не является високосным годом.")
    else:
        print(f"{year} является високосным годом.")
else:
    print(f"{year} не является високосным годом.")



'''Задание 2. Проверка с дополнительными условиями elif
'''
if year % 400 == 0:
    print(f"{year} является високосным годом.")
elif year % 100 == 0:
    print(f"{year} не является високосным годом.")
elif year % 4 == 0:
    print(f"{year} является високосным годом.")
else:
    print(f"{year} не является високосным годом.")

'''Задание 3. Проверка с помощью логических операторов в одну строку if'''
is_leap = "является високосным годом." if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else "не является високосным годом."
print(f"{year} {is_leap}")
'''Задание 4. Проверка с применением специальной функции модуля calendar
Найдите ее самостоятельно....
'''
import calendar
is_leap_calendar = calendar.isleap(year)
print(f"{year} является високосным годом." if is_leap_calendar else f"{year} не является високосным годом.")