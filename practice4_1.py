'''Упражнение 1. Поиск слова в текстовом файле
В этом упражнении вы реализуете программу, которая принимает от пользователя
поисковый запрос и выводит названия текстовых файлов, содержащих искомую
подстроку.
Предполагается, что все файлы располагаются в директории: PythonPrim Textfiles –
создайте эти папки и файлы для просмотра (любого типа).'''

import os

folder = r'C:\Users\unypo\Desktop\Main'
answ = set()
search = input("Enter the search bar: ")

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding='utf-8') as cur_file:
            for line in cur_file:
                if search in line:
                    answ.add(filename)

for file in answ:
    print(file)