zoo = ('питон', 'слон', 'пингвин') #скобки не обязательны
print('Количество животных в зоопарке -', len(zoo))

new_zoo = 'обезьяна', 'енот', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезенные из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезенное из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo)-1 + len(new_zoo[2]))
