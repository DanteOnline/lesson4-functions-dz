import os
import shutil
import pathlib
from sys import platform
from borndayforewer import victoryna
from use_functions import bank
author = 'Анатолий'
FILE_NAME = 'listdir.txt'
while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. сохранить содержимое рабочей директории в файл')
    print('13. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        dir_ = input('Введите введите название папки:')
        os.mkdir(dir_)
    elif choice == '2':
        dir_ = input('Введите введите название файл/папку:')
        if os.path.exists(dir_):
            file = pathlib.path(dir_)
            file.unlink()
        else:
            print('нет такой папки')

    elif choice == '3':
        nameCopy = input('Введите что копировать файл/папку:')
        nameResult = input('Введите новое название файл/папку:')
        shutil.copy(
            nameCopy,
            nameResult
        )
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':
        listOfDir = [f for f in os.listdir() if not os.path.isfile(f)]
        print(listOfDir)
    elif choice == '6':
        listOfFiles = [f for f in os.listdir() if os.path.isfile(f)]
        print(listOfFiles)
    elif choice == '7':
        print(platform)
    elif choice == '8':
        print('Создатель: ',author)
    elif choice == '9':
        victoryna()
    elif choice == '10':
        bank()
    elif choice == '11':
        print('Текущая директория:',os.getcwd())
        dir_ = input('Введите введите директорию для смены:')
        if os.path.exists(dir_):
             os.chdir(dir_)
        else:
            print('нет такой директории')
    elif choice == '12':
        with open(FILE_NAME, 'w') as f:
            listOfDir = ','.join([f for f in os.listdir() if not os.path.isfile(f)])
            listOfFiles = ','.join([f for f in os.listdir() if os.path.isfile(f)])
            f.write(f'files: {listOfFiles}\\n')
            f.write(f'dirs: {listOfDir}\\n')

    elif choice == '13':
        break

    else:
        print('Неверный пункт меню')
