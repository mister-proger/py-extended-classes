from main import MultiKeyDict

print('----- Инициализация -----')
my_dict: MultiKeyDict = MultiKeyDict()
my_dict['123'] = 101
my_dict['double'] = 102
my_dict.set_alias('double', 'test-alias')

print('----- Добавление элемента -----')
print(my_dict) # {('123',): 100, ('double', 'test-alias'): 100}
my_dict['double'] = 103
print(my_dict) # {('123',): 100, ('double',): 123, ('test-alias',): 100}

print('----- Создание алиаса -----')
my_dict.set_alias('123', 'test-to-key')
print(my_dict) # {('123', 'test-to-key'): 100, ('double',): 123, ('test-alias',): 100, ('256',): 123}

print('----- Удаление элемента -----')
del my_dict['123']
print(my_dict) # {('double',): 123, ('test-alias',): 100, ('test-to-key',): 100, ('256',): 123}

print('----- Методы словаря -----')
print(my_dict.keys()) # ('double', 'test-alias', 'test-to-key')
print(my_dict.values()) # (101, 102, 103)
print(my_dict.items()) # ((('double',), 103), (('test-alias',), 102), (('test-to-key',), 101))
print(dict(**my_dict)) # {'double': 103, 'test-alias': 102, 'test-to-key': 101}

print('----- Сопряжение -----')
print('До:', my_dict._keys, my_dict._values) # До: {'double': 3, 'test-alias': 2, 'test-to-key': 1} {1: 101, 2: 102, 3: 103}
my_dict.pairing('double', 'test-alias')
print('После:', my_dict._keys, my_dict._values) # После: {'double': 3, 'test-alias': 3, 'test-to-key': 1} {1: 101, 3: 103}
