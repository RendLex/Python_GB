# 1. Написать функцию 'email_parse(<email_address>)', которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Техническое задание:
#
# Функция:
# принимает параметр: строка email, при необходимости и другие параметры
# извлекает имя пользователя - то, что до знака @ и домен - то, что после знака @
# возвращает словарь вида {'username': <имя_пользователя>, 'domain': <домен>}
# Если адрес не валиден, выбросить исключение 'ValueError'. Можно с сообщением вида «wrong email: <email_address>»
# Шаблон имени пользователя: латинские буквы, цифры и символы: '._+-
# Шаблон домена: латинские буквы, цифры и символы .-
# В домене обязательно должна быть хотя бы одна точка
# Не использовать методы строки для извлечения информации из email - только регулярные выражения
# email полностью парсится за «один проход». Используйте группы.
# Проверьте работоспособность функции на прилагаемых тестовых email (файл task_8_1_test_email.txt). Попытайтесь добиться, чтобы для всех примеров ваша программа работала правильно. Допускаются 2-3 рассогласования.
# Чтобы проверить работоспособность функции на разных данных, вам придется «ловить» исключение в основной программе и выводить сообщение.
import re
# Задаем шаблон поиска без учета Кирилици
mail_template = r"([\w\_\.'+-]+)@([\w\.-]+\.{1}[\w\.-]+)"

def email_parse(email, regex_template=mail_template):
    rez = re.fullmatch(regex_template, email)
    if rez is None:
        raise ValueError(f"wrong email: {email}")
    rez = rez.groups()
    return {'username': rez[0], 'domain': rez[1]}

lst_data = [
"user0_name@domenname.ru",
"user1'name@domenname.ru",
"user2.name@domenname.ru",
"user3+name@domenname.ru",
"user4-name@domenname.ru",
"user5=name@domenname.ru",
"user6*name@domenname.ru",
"user7&name@domenname.ru",
"user8^name@domenname.ru",
"user9%name@domenname.ru",
"user10$name@domenname.ru",
"user11#name@domenname.ru",
"user12_name@domenna.me.ru",
"user13_name@domennameru",
"user14_name@domen-name.ru",
"user16_name@domen+name.ru",
"user17_name@domen=name.ru",
"user18_name@domen)name.ru",
"user19_name@domen*name.ru",
"user20_name@domen/name.ru",
"user21_name@domen&name.ru",
"user22_name@domen%name.ru",
"Юзер23_name@domenname.ru",
"user24_name@доменname.ru",
"user25_name@domen,name.ru",
"user26_name@domen<name.ru",
"user27>name@domenname.ru",
]
for email in lst_data:
    print(f"{email:34s}", end = "")
    try:
        print(f"{email_parse(email)}")
    except ValueError:
        print(f"Error")