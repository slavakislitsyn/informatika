# TODO Напишите функцию для поиска индекса товара
def f(a, b): #создание функции
    for items_list in range (len(a)): #подсчет количества товаров
        if a[items_list] == b:#разбиение списка на отдельные товары
            return items_list


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'] #список

for find_item in ['банан', 'груша', 'персик']: #поиск среди определенных товаров
    index_item = f(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:#условие того что товар найден
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
