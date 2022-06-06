# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
# |   |--settings
# |   |--mainapp
# |   |--adminapp
# |   |--authapp
#
# Техническое задание
#
# Продумайте ситуацию, когда все или часть этих папок уже есть в директории.
# Выберите наиболее подходящую структуру данных для хранения имен папок так, чтобы легко расширить количество создаваемых папок, например до 100 папок.
# Примечание:
#
# Можно ли будет расширять конфигурацию и хранить данные о вложенных папках и файлах?

from os import makedirs
from os.path import join, exists

main_dir = "my_project_07_01"
sub_dirs = ["settings", "mainapp", "adminapp", "authapp" ]
main_path = join(".", main_dir)

for sub_dir in sub_dirs:
    sub_path = join(".", main_dir, sub_dir)
    if not exists(sub_path): makedirs(sub_path)