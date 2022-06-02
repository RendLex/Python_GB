# 4. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# Техническое задание
#
# Все файлы этого задания хранить в отдельной директории, например «task_4» или на ваш выбор.
# Данные хранить в файле bakery.csv в кодировке utf-8.
# Соблюдаем формат данных в файле: одна запись (цифра) это одна строка.
# Для простоты все суммы продаж - целые числа.
# Запись в файл новых данных:
# Имя исполняемого скрипта: task_4_add_sale.py
# При записи передавать из командной строки значение суммы продаж. Функцию input не использовать.
# Новая запись дозаписывается в конец файла.
# Корректно обработать неправильное количество или тип переданных параметров.
# Вывод на экран записей:
# Имя исполняемого скрипта: task_4_show_sales.py
# Предполагаем, что первая запись имеет номер 1.
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи от номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная от номера, равного первому числу, по номер, равный второму числу, включительно; Если второе число больше, чем количество записей в файле - просто выводить до конца.
# Корректно обработать неправильное количество или тип переданных параметров.
# Примеры/Тесты:
# Примеры запуска скриптов:
#
#
# python add_sale.py 5978
# python add_sale.py 891
# python add_sale.py 7879
# python add_sale.py 1573
# python show_sales.py
# 5978
# 891
# 7879
# 1573
# python show_sales.py 3
# 7879
# 1573
# python show_sales.py 1 3
# 5978
# 891
# 7879
from sys import argv

def show_lines(file, begin = None, end = None):

    for idx, line in enumerate(file):
        is_begin_norm = (begin is not None and idx >= begin-1) or begin is None
        is_end_norm = (end is not None and idx <= end-1) or end is None
        if is_begin_norm and is_end_norm:
            print(line.strip())

# Для отладки:
# argv = [""]
# argv = ["",1]
# argv = ["",1,3]

len_argv = len(argv)
with open("bakery.csv", encoding="UTF-8", mode="rt") as file:
    if len_argv == 1:
        print("Все записи:")
        show_lines(file, begin = None, end = None)
    elif len_argv == 2:
        record_begin = int(argv[1])
        print(f"Записи из списка c {record_begin}:")
        show_lines(file, begin = record_begin, end = None)
    else:
        record_begin = int(argv[1])
        record_end = int(argv[2])
        print(f"Записи из списка с {record_begin} по {record_end}")
        show_lines(file, begin = record_begin, end = record_end)