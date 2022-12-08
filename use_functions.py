"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import json
import os

FILE_ACCOUNTS = 'accounts.json'
FILE_HISTORY = 'history.json'


def save_account(summ):
    accounts = {1: summ}
    with open(FILE_ACCOUNTS, 'w') as f:
        json.dump(accounts, f)


def save_history(hist):
    with open(FILE_HISTORY, 'w') as f:
        json.dump(hist, f)


def bank():
    if os.path.exists(FILE_ACCOUNTS):
        with open(FILE_ACCOUNTS, 'r') as f:
            result = json.load(f)
            cash = result['1']
    else:
        cash = 0
    if os.path.exists(FILE_HISTORY):
        with open(FILE_HISTORY, 'r') as f:
            history = json.load(f)
    else:
        history = {}
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            summ = input('Введите сумму:')
            cash += int(summ)
        elif choice == '2':
            bay = input('Введите сумму:')
            if int(bay) <= cash:
                purchase = input('Введите товар:')
                history[purchase] = int(bay)
                cash -= int(bay)
        elif choice == '3':
            for elem in history:
                print(f'{elem}: {history[elem]} руб.')
        elif choice == '4':
            save_account(cash)
            save_history(history)
            break
        else:
            print('Неверный пункт меню')

