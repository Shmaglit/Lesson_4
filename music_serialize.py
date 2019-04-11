# 1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
#
# my_favourite_group = {
# 'name': 'Элизиум',
# 'tracks': ['Последний месяц осени', 'Шапито'],
# 'Albums': [{'name': 'Делать панк-рок','year': 2016},
# {'name': 'Шапито','year': 2014}]}
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.


import json
import pickle

my_favourite_group = {
'name': 'Элизиум',
'tracks': ['Космос', 'Бесконечность', ''],
'Albums': [{'name': 'Космос','year': 2003},
{'name': 'На окраинах вселенной','year': 2005}]}

# преобразование в json
group1 = json.dumps(my_favourite_group)
print(group1)
print(type(group1))

with open('group.json','w', encoding='utf-8') as f:
    # запись json в файл
    #f.write(groupe1)
    json.dump(my_favourite_group, f)

# преобразование в pickle
group2 = pickle.dumps(my_favourite_group)
print(group2)
print(type(group2))

with open('group.pickle','wb') as f:
   #  запись pickle в файл
    #f.write(groupe2)
    pickle.dump(my_favourite_group, f)



