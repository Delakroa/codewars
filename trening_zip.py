import os
import zipfile


def main_data():
    """Получаем список файлов из дериктории"""
    file_list = os.listdir("d:\\инстр по линии")
    return file_list


def data_zip():
    """Архивируем файлы"""
    data = zipfile.ZipFile("d:\\инстр по линии\\jungle.zip", "w")
    data.write("d:\\инстр по линии\\jungle.zip", compress_type=zipfile.ZIP_DEFLATED)

    data.close


print(main_data())
data_zip()
