# -*- coding: utf8 -*-
import os
import sys
import shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def mk_dir():
    for i in range(1,10):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Такая директория уже существует')
def rm_dir():
    for i in range(1,10):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print('Такой директории не существует')

# mk_dir()
# rm_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории

def list_dir():
    print([i for i in os.listdir(os.getcwd()) if os.path.isdir(i)])

# list_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    this_fail = str(os.path.basename(str(sys.argv))).replace("']","")
    shutil.copy(str(this_fail), 'new.py')
# copy_file()