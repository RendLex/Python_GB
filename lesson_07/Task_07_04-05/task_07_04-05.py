# 4. Написать скрипт, который для заданной папки выводит статистику размеров файлов
# Техническое задание
# Директорию с файлами 'some_data' можно скачать из прикрепленных к уроку файлов.
# Результат формируется в виде словаря
# ключи — верхняя граница размера файла.
# значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)
# Границы диапазонов размеров считаем фиксированными данными - пусть будет кратна 10, как в примере.
# Программа должна легко модифицироваться под другие границы диапазонов.
# Программа должна легко модифицироваться под увеличение количества диапазонов. Т.е. если диапазонов станет 150 шутк - не надо будет переписывать всю программу.
# Формат вывода результата:
# {
#   100: 15,
#   1000: 3,
#   10000: 7,
#   100000: 2
# }
#
# Примечание:
#
# В примере: Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# 5. [Задача со звездочкой]: усложненный вариант задания 4. Написать скрипт, который для заданной папки выводит статистику размеров файлов по расширениям.
# Техническое задание
#
# Директорию с файлами 'some_data_adv' можно скачать из прикрепленных к уроку файлов.
# Результат формируется в виде словаря
# ключи — верхняя граница размера файла (пусть будет кратна 10) - как в задании 4.
# значения — списки вида '[<files_quantity>, [<files_extensions_list>]]'. В список '<files_extensions_list>' заносятся все расширения для файлов удовлетворяющих условию размера, без повторений.
# Словарь сохраните в файл '<folder_name>_summary.json' в той же папке, где запустили скрипт.
# Формат вывода результата:
# {
#     100: [15, ['txt']],
#     1000: [3, ['py', 'txt']],
#     10000: [7, ['html', 'css']],
#     100000: [2, ['png', 'jpg']]
#   }
from os import walk, stat
from os.path import join, abspath
from json import dumps

root_dir = join(".")
# Выбираем файл для анализа
# data_dir = join(root_dir, "some_data")
data_dir = join(root_dir, "some_data_adv")

# По условию код должен быть просто расшиярем.
size_bounds = [100, 1000, 10000, 100000]

# Создадим словарь
size_dict = {s: 0 for s in size_bounds}
for root, dirs, files in walk(data_dir):
    for file in files:
        file_size = stat(join(root, file)).st_size
        for size in size_dict.keys():
            if file_size <= size:
                size_dict[size] += 1
                break  # break обязателен
print(size_dict)

size_dict = {s: [0, list(), dict()] for s in size_bounds}

for root, dirs, files in walk(data_dir):
    for file in files:
        file_size = stat(join(root, file)).st_size
        file_ext = file.split(".")[-1]
        for size in size_dict.keys():
            if file_size <= size:
                if file_ext not in size_dict[size][1]:
                    size_dict[size][1].append(file_ext)
                size_dict[size][2][file] = file_size
                size_dict[size][0] +=1
                break  # break обязателен
with open(join(root_dir, f"{data_dir}_summary.json"), encoding="utf-8", mode="wt") as file:
    file.write(dumps(size_dict, indent=2))