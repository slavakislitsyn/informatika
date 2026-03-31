

# TODO импортировать необходимые модули
import csv #
import json #

INPUT_FILENAME = "input.csv" #
OUTPUT_FILENAME = "output.json" #


def task() -> None: #объявление функции с указателем None
    # TODO считать содержимое csv файла
    spisoc = [] #создание пустого списка
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file: # преобразование файла с кодировкой
        csv_reader = csv.DictReader(csv_file, delimiter=',') #создает объект DictReader, который читает файл и преобразует строчки в список

        for i in csv_reader:#проверка в csv_reader
            spisoc.append(i) #добавление переменнрой в список, созданный ранее

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:# преобразование файла с кодировкой
        json.dump(spisoc, json_file, indent=4, ensure_ascii=False) #сохранение данных с отступом в файл с форматированием.


if __name__ == "__main__":
    task() #проверка на то, запущен ли файл как основная программа или импортирован как модуль.

with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f: # преобразование файла с кодировкой
    for line in output_f: #проверка в output_f
        print(line, end="") # вывод ответа