# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates:
#
# |--my_project
# ...
# |--templates
# |   |--mainapp
# |   |  |--base.html
# |   |  |--index.html
# |   |--authapp
# |   |  |--base.html
# |   |  |--index.html
#
# Техническое задание
#
# Шаблон - это папка templates в исходной структуре папок. Ее уровень в структуре папок может быть любым. В папках mainapp, authapp и аналогичных могут быть и другие файлы, с другими раширениями, кроме тех что приведенны в примере.
# Папку templates надо создать внутри исходной директории, в примере - внутри my_project
# Исходные файлы и папки необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён).
# Предусмотреть возможные исключительные ситуации;
# Примечание:
#
# это вполне реальная задача, которая решена, например, во фреймворке django.
from os import listdir, walk
from os.path import join
from shutil import copytree

root_dir = join(".")
base_prj_dir = listdir(root_dir)[0]  # Считаем, что в корне - одна директория
templates_dir = join(root_dir, base_prj_dir, "templates")
for root, dirs, files in walk(root_dir):
    print(root, dirs, files)
    if "templates" in dirs:
        copytree(join(root, "templates"), templates_dir, dirs_exist_ok = True)