'''
1. Создайте программу и добавьте следующий код, реализующий ядро игры
(обратите внимание на использование модулей random и time):
from random import randint
import time
#Ввод имен играющих
gamer1 = input('Введите имя 1-го играющего ')
gamer2 = input('Введите имя 2-го играющего ')
#Моделирование бросания кубика первым играющим
print('Кубик бросает', gamer1)
time.sleep(2)
n1 = randint(1, 6)
print('Выпало:', n1)
#Моделирование бросания кубика вторым играющим
print('Кубик бросает', gamer2)
time.sleep(2)
n2 = randint(1, 6)
print('Выпало:', n2)
2. Реализуйте определение победителя игры. Для этого используйте оператор
if elif else для реализации выбора из нескольких альтернатив.
Возможное решение:
#Определение результата (3 возможных варианта)
if n1 > n2:
print('Выиграл', gamer1)
elif n1 < n2:
print('Выиграл', gamer2)
else:
print('Ничья')
3. Запустите игру и проверьте работу программы.
'''


'''
from random import randint
import time


gamer1 = input('Введите имя 1-го играющего: ')
gamer2 = input('Введите имя 2-го играющего: ')


print('Кубик бросает', gamer1)
time.sleep(2)
n1 = randint(1, 6)
print('Выпало:', n1)


print('Кубик бросает', gamer2)
time.sleep(2)
n2 = randint(1, 6)
print('Выпало:', n2)


if n1 > n2:
    print('Выиграл', gamer1)
elif n1 < n2:
    print('Выиграл', gamer2)
else:
    print('Ничья')

'''

'''2. Использование циклов
Добавьте в разработанную программу возможность бросать кубик игрокам
несколько раз и по итогам этих бросков определять победителя (например, по
количеству побед в сеансах или по общей сумме очков).
Предположим, что игроки заранее договорились о числе партий (бросков). В
таком случае подходящим циклом будет цикл for.
1. Добавьте в программу цикл for, реализующий 5 партий (бросков):
for i in range(5):
#Моделирование бросания кубика первым играющим
...
Обрате внимание на указание отступов (4 пробела) для тела цикла.
2. Добавьте реализацию определения победителя. Например, с помощью
подсчета количества побед каждым игроком, или суммированием очков.
3. После цикла добавьте оператор ветвления для определения итогового
победителя.'''

'''
from random import randint
import time
gamer1 = input('Введите имя 1-го играющего: ')
gamer2 = input('Введите имя 2-го играющего: ')
score1 = 0
score2 = 0
rounds = 5

for i in range(rounds):
    print(f"Раунд {i+1}")
    print('Кубик бросает', gamer1)
    time.sleep(2)
    n1 = randint(1, 6)
    print('Выпало:', n1)

    print('Кубик бросает', gamer2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало:', n2)


    if n1 > n2:
        print('Выиграл', gamer1)
        score1 += 1
    elif n1 < n2:
        print('Выиграл', gamer2)
        score2 += 1
    else:
        print('Ничья')

    print(gamer1+' выиграл раундов: '+str(score1))
    print(gamer2+' выиграл раундов: '+str(score2))
    print()

# Определение итогового победителя
if score1 > score2:
    print('Итоговый победитель:', gamer1)
elif score1 < score2:
    print('Итоговый победитель:', gamer2)
else:
    print('Итоговая ничья')'''

'''Дополнительное задание
Создайте игрока, с помощью словаря (см. предыдущие задания) и после игры
сохраните результаты с привязкой к конкретному игроку. Подумайте, какие
атрибуты могут быть у игрока кроме имени, которые могли бы содержать
информацию о результатах игры.
Результаты игры выведите на экран и сохраните в файл (тип файла выберите
самостоятельно, обоснуйте свой выбор).'''
from random import randint
import time
import json


def create_player(name):
    return {"name": name, "wins": 0, "total_score": 0, "rolls": []}


name1 = input('Введите имя 1-го играющего: ')
name2 = input('Введите имя 2-го играющего: ')


player1 = create_player(name1)
player2 = create_player(name2)
rounds = 5


for i in range(rounds):
    print(f"Раунд {i + 1}")
    print(f"Кубик бросает {player1['name']}")
    time.sleep(1)
    n1 = randint(1, 6)
    player1['rolls'].append(n1)
    player1['total_score'] += n1
    print('Выпало:', n1)

    print(f"Кубик бросает {player2['name']}")
    time.sleep(1)
    n2 = randint(1, 6)
    player2['rolls'].append(n2)
    player2['total_score'] += n2
    print('Выпало:', n2)

    if n1 > n2:
        print('Выиграл', player1['name'])
        player1['wins'] += 1
    elif n1 < n2:
        print('Выиграл', player2['name'])
        player2['wins'] += 1
    else:
        print('Ничья')


if player1['wins'] > player2['wins']:
    print('Итоговый победитель:', player1['name'])
elif player1['wins'] < player2['wins']:
    print('Итоговый победитель:', player2['name'])
else:
    print('Итоговая ничья')


results = {"players": [player1, player2]}
with open('game_results.json', 'w') as file:
    json.dump(results, file)


#print('Результаты игры:')
#print(json.dumps(results, indent=4))