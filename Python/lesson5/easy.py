# -*- coding: utf8 -*-
import os


def make_dir(dir_path):
    try:
        os.mkdir(dir_path)
        print('Успешно создана')
    except FileExistsError:
        print('Директория уже существует\n Невозможно создать!')


def list_dir():
    return os.listdir(os.getcwd())



def rm_dir(dir_path):
    try:
        os.rmdir(dir_path)
        print('Успешно удалено')
    except FileNotFoundError:
        print('Такой директории не существует\n Невозможно удалить!')