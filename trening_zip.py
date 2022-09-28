import os
import zipfile


def go_to_directory():
    """Переходим в рабочую директорию"""
    os.chdir("d:\\инстр по линии")
    print(os.listdir())


def data_zip():
    """Архивируем файлы"""
    # Обращаемся к модулю для архивации дальнейших записываемых данных
    zip_file = zipfile.ZipFile("d:\\инстр по линии\\archive.zip", "w")
    # Записываем в архив файл.
    # Рекурсивный проход по папкам и подпапкам.
    # folder - удержать исходное место откуда мы проходим.
    # sub_folder - все папки и подпапки.
    # files - все файлы в этих папках и подпапках.
    for folder, sub_folder, files in os.walk("d:\\инстр по линии"):
        for file in files:
            if file.endswith(('.pdf', 'doc')):  # Метод возвращает True, если строка заканчивается указанным значением.
                zip_file.write(os.path.join(folder, file),
                               os.path.relpath(os.path.join(folder, file), "d:\\инстр по линии"),
                               compress_type=zipfile.ZIP_DEFLATED)

    zip_file.close()


go_to_directory()
data_zip()
print(os.listdir())
