'''Project 1_5B
Указания:
• для каждой задачи данного раздела сначала создаются функции, а затем,
используя их, выполняется решение задачи;
• ввод и вывод данных для функции необходимо обеспечить самостоятельно;
• для каждой написанной функции нужно использовать строки документации;
• при выводе вещественных результатов оставьте два знака после запятой.
'''

'''Задания:
1. Дан список температурных изменений в течение дня (целые числа). Известно,
что измеряющее устройство иногда сбоит и записывает отсутствие
температуры (значение None). Выведите среднюю температуру за
наблюдаемый промежуток времени, предварительно очистив список от
неопределенных значений. Гарантируется, что хотя бы одно определенное
значение в списке есть.'''


def calculate_average_temperature(temperatures):
    filtered_temperatures = [temp for temp in temperatures if temp is not None]
    average_temperature = sum(filtered_temperatures) / len(filtered_temperatures)
    return round(average_temperature, 2)


temperatures = [23, 20, None, 25, 22, None, 19, 29, 29, 28]
print("Средняя температура:", calculate_average_temperature(temperatures))

'''
2. Напишите функцию, которая принимает неограниченное количество
числовых аргументов и возвращает кортеж из двух списков: отрицательных
значений (отсортирован по убыванию); неотрицательных значений
(отсортирован по возрастанию).
'''
def sort_numbers(*args):

    negative_numbers = sorted([num for num in args if num < 0], reverse=True)
    positive_numbers = sorted([num for num in args if num >= 0])
    return (negative_numbers, positive_numbers)


print("Результат сортировки чисел:", sort_numbers(-1,3,55,12,123,-3,1,0,12,99,-1003))


'''
3. Составьте две функции для возведения числа в степень: один из вариантов
реализуйте в рекурсивном стиле.'''

def power_recursive(number, degree):
    if degree == 0:
        return 1
    elif degree > 0:
        return number * power_recursive(number, degree - 1)
    else:
        return 1 / power_recursive(number, -degree)

def power_iterative(number, degree):
    result = 1
    for _ in range(abs(degree)):
        result *= number
    return result if degree >= 0 else 1 / result

print("Рекурсивное возведение в степень:", power_recursive(2, -8))
print("Итеративное возведение в степень:", power_iterative(2, -8))