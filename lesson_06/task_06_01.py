# 1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Техническое задание
#
# Не использовать библиотеки для парсинга. Только работа со строками.
# Создать список кортежей вида: '(<remote_addr>, <request_type>, <requested_resource>)'. Именно список кортежей.
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Вывести список на экран.
# Формат вывода результата:
#
#
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_1'),
#     ...
# ]
list_string = []

file = open("nginx_logs.txt", mode="rt", encoding="UTF-8")

for line in file:
    line1, line2, *_ = line.split('"')
    line1, line2 = line1.split(), line2.split()
    list_string.append((line1[0], line2[0], line2[1]))

for el in list_string:
    print(el)

file.close()