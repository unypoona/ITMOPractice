'''Упражнение 4 (контрольное). Перемещение файлов в требуемый каталог
Напишите программу, которая должна будет запускаться в командной строке в
текущем рабочем каталоге с передачей ей параметра – имени каталога, в который
будут перенесены текстовые файлы текущего рабочего каталога.
Формат вызова в командной строке из текущего рабочего каталога:
Имя_программы.ру Имя_каталога
В программе сначала требуется создать требуемый каталог, затем перенести в него
все текстовые файлы. Для реализации этого использовать только функциональность
модуля pathlib:
from pathlib import Path
Для реализации передачи имени каталога как параметра в командной строке:
from sys import argv
dir_name = argv[1] # первый параметр - имя каталога'''

# Импортируем необходимые модули
from pathlib import Path
from sys import argv


def main():
    if len(argv) != 2:
        print("Usage: python имя_программы.py имя_каталога")
        return

    target_directory = argv[1]

    target_path = Path(target_directory)

    target_path.mkdir(exist_ok=True)

    current_directory = Path('..')

    text_files = current_directory.glob('*.txt')

    for file in text_files:
        destination = target_path / file.name
        file.rename(destination)
        print(f"Moved {file} to {destination}")


if __name__ == "__main__":
    main()
