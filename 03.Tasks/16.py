# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A i. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
from random import randint
# Я вывожу как в тех.задании без текста, типа "введите число" и т.д.
# следовательно вывод максимально приближен к заданию!
size_n = int(input()) # ввод числа N - размер массива
array_a = [randint(1,10) for _ in range(size_n)] # генератор случайного списка (массива A)
print(*array_a) # вывод содержимого массива A (списка)
number_x = int(input()) # ввод числа X - искомого числа
print(f"-> {array_a.count(number_x)}") # вывод количества совпадений X в массиве
