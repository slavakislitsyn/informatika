# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):#создание функции
    list1 = group1.split(separator)#первый список участников
    list2 = group2.split(separator)#второй список
    common = []#создание пустого списка
    for name in list1:#прогон именит через первый список
        if name in list2:#если оно есть так же и во втором списке
            common.append(name)#добавляем в созданный список
    return sorted(common)#сортировка по алфавиту

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, '|')#получение итогового результата засчет созданной ранее функции
print(result)



# TODO Провеьте работу функции с разделителем отличным от запятой
