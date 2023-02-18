# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - 
# элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# import random
# len_n = random.randint(5,10)
# len_m = random.randint(5,10)
# array_n = [random.randint(5,10) for i in range(len_m)]
# array_m = [random.randint(5,10) for i in range(len_m)]
# print(*array_n)
# print(*array_m)
# for i in array_n:
#     if i not in array_m:
#         print(i, end=" ")
list1 = [int(input(f'Введите {i + 1}-е число: ')) for i in range(int(input('Введите количество элементов первого массива: ')))]
list2 = [int(input(f'Введите {j + 1}-е число: ')) for j in range(int(input('Введите количество элементов второго массива: ')))]
new_list = [el if el not in list2 else 0 for el in list1] 
print(new_list)