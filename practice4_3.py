'''Упражнение 3. Применение модуля pathlib для создания файлов и папок
В этом упражнении вы будете использовать модуль pathlib, который упрощает
работу с файлами и папками. Он является частью стандартной библиотеки Python
начиная с версии 3.4 и сочетает в себе лучшее из модулей файловой системы Python –
os, os.path, glob и других, собирает необходимый функционал в одном месте и делает
его доступным через методы и свойства Path-объекта.
Требуется реализовать следующие действия:
1. Создать новую директорию.
2. В новую директорию добавить (создать) файлы, например, два текстовых
файла и один файл изображения.
3. Создать еще одну новую директорию внутри первой.
4. Переместить файл изображения в созданную директорию.'''

from pathlib import Path

home = Path.home()
my_folder = home / r'C:\Users\unypo\Desktop\Main'

if not my_folder.exists():
    my_folder.mkdir()

file1 = my_folder / "file1.txt"
file1.touch()

(my_folder / "file2.txt").touch()

image_file = my_folder / "image.png"
image_file.touch()
image_file = my_folder / "image.jpg"
image_file.touch()

images_folder = my_folder / "images"
images_folder.mkdir(exist_ok=True)

for f in my_folder.glob('*.png'):
    path_destination = Path(my_folder /"images") / f.name
    f.replace(path_destination)

print("Directories have been created and files have been successfully added and moved.")