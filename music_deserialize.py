#2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию. Получить объект — словарь из предыдущего задания.

import json
import pickle

with open('group.json','r', encoding='utf-8') as f:
    groupe = json.load(f)
    print(groupe)
    print(type(groupe))


with open('group.pickle','rb') as f:
    groupe1 = pickle.load(f)
    print(groupe1)
    print(type(groupe1))
