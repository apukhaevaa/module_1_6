# Пухаева Алина Александровна
#  Dictionaries and data sets.
# 28.08.2024
# Notes: ctrl+alt+L

# task 2
my_dict = {'Анастасия': 1993, 'Дмитрий': 1992, 'Екатерина': 1990, 'Олег': 1989}
print(my_dict)
print(my_dict.get('Екатерина', 'Нет значения'))
print(my_dict.get('Анна', 'Нет значения'))
my_dict.update({'Павел': 1995, 'Вероника': 2000})
print(my_dict)
my_dict.pop('Анастасия')
print(my_dict)
# task 3
my_set = {11, 12, 11, 15, 12, False, 'France', 'Spain', 'France'}
print(my_set)
my_set.update({7, (9, 6)})
print(my_set)
my_set.discard(12)
print(my_set)