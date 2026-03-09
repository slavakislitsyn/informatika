list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2 #подсчет числа игроков в каж+дой команде

first_team = list_players[:middle_index] #распределение игроков в первую команду до найденного числа игроков
second_team = list_players[middle_index:] #распределение игроков во вторую команду после найденного числа игроков

print(first_team)
print(second_team)
