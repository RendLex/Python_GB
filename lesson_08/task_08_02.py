# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# Техническое задание:
#
# Лог файл: https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# Функция парсинга строки лог-файла:
# Принимает параметр: строка для пасинга, при необходимости и другие параметры
# возвращает кортеж из 6 элементов вида: ('<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)'
# Вы можете не обращать внимание на IPv6 или явно учесть их в регулярном выражении, это будет очень хорошо.
# Проверьте работоспособность функции на нескольких строках лог файла.
# Распарсите весь файл и сформируйте список всех IP лог файла, без повторений. Выведите в консоль его длину.
# Усложнение:
#
# Ваша функция должна корректно обрабатывать как IPv4, так и IPv6 - найдите их в лог-файле.
# Посмотрите спецификацию IPv6. Что такое шестнадцатеричное число и какие буквы/цифры оно может включать. Сколько их может быть в IPv6.
# Совсем хорошо, если вы обработаете cокращенные адреса IPv6, которые тоже в есть в лог файле.
# Ваш шаблон должен пропускать только то, что нужно, не используйте «избыточно широкие» шаблоны.
import re

log_string_template = re.compile("""
((?:([\d]{1,3}\.){3}[\d]{1,3})|(?:([a-f0-9]{0,4}:){4,8}[a-f0-9]{0,4}))      # Это IPv4 или IPv6
[\s-]+            # Пробелы и тире
\[(.+)\]          # Дата и время: то, что в квадратных скобках
\s\"
(\w+)             # Вид запрос: GET, POST или другой
\s
([\/\w]+)         # ресурс
\sHTTP\/[\d\.]+
\"\s
(\d{3})\s         # код ответа
(\d)+             # размер ответа
""", re.VERBOSE)

def log_string_parse(log_string, regex_template):
    rez = regex_template.search(log_string)
    if rez is not None:
        rez = rez.groups()
    else:
        raise ValueError
    return rez[0], rez[3], rez[4], rez[5], rez[6], rez[7]

ip_all = set()
with open("nginx_logs.txt", encoding="UTF-8", mode="rt") as file:
    for line in file:
        try:
            ip, *_= log_string_parse(line, log_string_template)
            ip_all.add(ip)
        except ValueError:
            print(f"Строка не по шаблону: {line}")

lst_all_ip = list(ip_all)
print(f"Длина списка IP без повторений: {len(lst_all_ip)}")
