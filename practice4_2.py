'''Упражнение 2 (контрольное). Получение информации о файле
В этом упражнении требуется реализовать вывод следующей статистики по тексту
из указанного файла:
• количество букв;
• число слов;
• число строк.
Пример ввода и вывода
Предположим, что file.txt содержит приведенный ниже текст:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
В этом случае программа должна вывести информацию о файле в следующем
виде:
Input file contains:
108 letters
20 words
4 lines
Рекомендации к решению
Чтение из файла можно реализовать с помощью функции read() – если ничего не
указать в качестве аргумента функции, то получится прочитать сразу все содержимое
документа.
Количество букв можно подсчитать функцией sum(), передав ей в качестве
параметра функцию map(), которая в свою очередь должна получить в качестве

3
параметров объект str.isalpha и содержимое файла.
Число слов – с помощью функции len(), принимающую список с разделенными
словами (split).
Число строк можно получить подсчетом, например символов новой строки.'''

filename = 'C:\\Users\\unypo\\Desktop\\Main\\file.txt'

try:

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # num_letters = sum(1 for char in content if char.isalpha())

    num_letters = sum(map(str.isalpha, content))
    words = content.split()
    num_words = len(words)

    num_lines = content.count('\n') + 1

    print(f"Input file contains:")
    print(f"{num_letters} letters")
    print(f"{num_words} words")
    print(f"{num_lines} lines")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

