from sys import argv
filename = argv[1]  # первый параметр - имя файла
names = argv[2:]    # остальные параметры

f1 = open(filename, 'w')
for it in names:                    # Запись всех параметров из списка в файл
    f1.write(it + '\t')
f1.close()

with open(filename, 'r') as fobj:
    content = fobj.readline()             # Читает содержимое как строку
    print(content)