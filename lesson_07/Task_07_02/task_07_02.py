# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать скрипт, создающий из config_2.yaml стартер для проекта со следующей структурой:
#
# |--my_project
# |  |--settings
# |  |  |--__init__.py
# |  |  |--dev.py
# |  |  |--prod.py
# |  |--mainapp
# |  |  |--__init__.py
# |  |  |--models.py
# |  |  |--views.py
# |  |  |--templates
# |  |  |  |--mainapp
# |  |  |  |  |--base.html
# |  |  |  |  |--index.html
# |  |--authapp
# |  |  |--__init__.py
# |  |  |--models.py
# |  |  |--views.py
# |  |  |--templates
# |  |  |  |--authapp
# |  |  |  |  |--base.html
# |  |  |  |  |--index.html
#
# Техническое задание
#
# Пример файла config_2.yaml можно скачать из прикрепленных к уроку файлов. Или его можно создать в любом текстовом редакторе «руками» (не программно).
# Не используйте библиотеки для работы с YAML, проведите парсинг вручную.
# Правильный парсинг yaml - интересная задача, но может быть сложной. В этой задаче примем: глубина иерархии в директории определяется количеством пробелов перед именем файла/директории; отличие директории о файла выберите сами: например в имени файла будет точка или после имени директории стоит двоеточие.
# Подумайте о возможных исключениях при работе скрипта.
from os import makedirs
from os.path import join, exists
from os import makedirs
from os.path import join, exists

def parse_yaml(src_string, space = 2):
    lst_yaml = src_string.split("-")
    name = lst_yaml[-1].strip(" \n")
    if name[-1] == ":":
        isfile = False
        name = name[:-1]
    else:
        isfile = True
    lenght = len(lst_yaml)
    # Проверка для элементов где нет пробелов спереди.
    if lenght > 1:
        level = len(lst_yaml[0]) // space
    else:
        level = 0
    return level, name, isfile

yaml_path = join(".", "config_2.yaml")
current_path = []
current_level = -1
with open(yaml_path, encoding="UTF-8", mode="rt") as file:
    for line in file:
        level, name, isfile = parse_yaml(line)
        if current_level < level:
            # Увеличение уровня вложенности
            current_path.append(name)
            current_level += 1
        elif current_level == level:
            # Тот  же уровень вложенности, но другой объект
            current_path[-1] = name
        else:
            # Уменьшение уровня вложенности
            for i in range(current_level-level+1):
                current_path.pop()
                current_level -= 1
            current_level += 1
            current_path.append(name)

        dir_path =  join(".", *current_path)
        if not exists(dir_path):
            if isfile:
                # Воспользуемся уневирсальным методом
                with open(dir_path, encoding= "UTF-8", mode = "w"):
                    pass
            else:
                makedirs(dir_path)