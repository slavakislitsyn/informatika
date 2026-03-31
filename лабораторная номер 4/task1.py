# TODO решите задачу
import json#открытие библиотеки
def task():#создание функции
    with open('input.json', 'r') as f:#открытие файла для чтения как отдельную переменную f
        data = json.load(f)#ввод переменной для чтения файла и преобразование его в формат, считываемый питоном
    summa = 0#ввод переменной
    for slovar in data:#поиск переменной в списке
        proizvedenie = slovar['score'] * slovar['weight']#умножение заданных величин
        summa += proizvedenie#суммирование
    return round(summa, 3)
print(task())