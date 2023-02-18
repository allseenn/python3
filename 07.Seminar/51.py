# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# def same_by(char, objects):
#     if (char, objects):
#         print("same")
#     else: 
#         print("different")

# def same_by(char, objects):
#      res = True
#      for i in list(map(char, objects)):
#         res &= i
#      return res
# characteristic = lambda x: x % 2 == 0
# values = [1, 1, 3, 5]
# print(same_by(characteristic, values))
def same_by(func, list1):
    new_list1 = list(filter(func, list1))
    return len(new_list1) == len(list1) or len(new_list1) == 0
values = [2, 4, 6, 8]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')