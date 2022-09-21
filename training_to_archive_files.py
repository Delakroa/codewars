# Задача
# 1. Открыть папку
# 2. Пропустить через цикл все объекты папки
# 3. Упаковать их.
# 4 Использовать название файла в качестве названия архива.
# 5. в конец установить флаг нижнее подчёркивание result.

import os
import zipfile


def main_zip():
    """Архивирование файлов"""
    path_to_archive = r'test.zip'
    path = r'd:\Soft\Торент загрузки\"'
    pattern = r'\babc.*\.mp.$'
    all_files = []
    with zipfile.ZipFile(path_to_archive, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for root_path, dirs, files in os.walk(path):
            for name in files:
                full_path = os.path.join(root_path, name)
                if os.path.isfile(full_path) and re.match(pattern, name):
                    if root_path == path:
                        zf.write(full_path, name)
                    else:
                        res = os.path.split(root_path)[-1]
                        zf.write(full_path, os.path.join(res, name))
                    all_files.append(full_path)
    print(os.path.abspath(path_to_archive))
    print('\n'.join(all_files))


def main_path():
    """Показывает содержимое директории"""
    print(f"Содержимое папки WinHex v19.9 Ml_Rus: ")
    for filename in os.listdir("d:/Soft/Торент загрузки/WinHex v19.9 Ml_Rus/"):
        print(f"--{filename}")


def file_name():
    """Иногда для взаимодействия с документом необходимо получить его полное имя,
    включающее разрешение, но не абсолютный путь к нему на диске.
    Преобразовать адрес объекта в название позволяет функция basename, которая содержится в
    подмодуле path из библиотеки os. Таким образом, следующий пример показывает преобразование
    пути test.txt в простое имя файла"""

    print("Получение полного имени:")
    return print("----", os.path.basename("d:/Лечение.txt"))


def dir_name():
    """Обратная ситуация возникает тогда, когда пользователю нужно получить только путь к файлу,
    без самого названия объекта. Это поможет сделать метод dirname, который возвращает путь к заданному
    документу в строковом представлении, как это продемонстрировано в небольшом примере ниже.
    Здесь print выводит на экран адрес текстового документа в папке folder."""
    print("Отображение пути:")
    return print(os.path.dirname(r"d:\Soft\Торент загрузки\WinHex v19.9 Ml_Rus\Documentation"))


def path_check():
    """Проверяет есть ли путь на самом деле"""
    print("Проверка пути (True или False?):")
    return print(os.path.exists("d:/Soft/Торент загрузки/WinHex v19.9 Ml_Rus/"))


main_path()
print("----" * 10)
file_name()
print("----" * 10)
dir_name()
print("----" * 10)
path_check()
