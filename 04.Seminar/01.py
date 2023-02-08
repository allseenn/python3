my_dict = {'Иванов':'Петр', 'Петров': 'Иван', (1, 2, 3 ,4): 'это числа', 
True: True, 123: [234,345,456,567], None: 'я не пустое место!', 
2: [1,2, [10, 20, [100, 200]]]}
print(my_dict)

my_dict['Иванов'] = 'Вася'
print(my_dict)
my_dict['Иванов'] += '-Вася'
print(my_dict)

my_dict['Сидоров'] = my_dict.pop('Петров')
print(my_dict)

print(my_dict.get(1234, 0))
print(my_dict[123][2])
print(my_dict[2][-1][2][0])