# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A i. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint
# Я вывожу как в тех.задании без текста, типа "введите число" и т.д.
# следовательно вывод максимально приближен к заданию!
MAXIMUM = 10 # Максимальное целое число
size_n = int(input()) # ввод числа N - размер массива
array_a = [randint(1,MAXIMUM) for _ in range(size_n)] # генератор случайного списка (массива A)
print(*array_a) # вывод содержимого массива A (списка)
number_x = int(input()) # ввод числа X - искомого числа
plus = [i-number_x for i in array_a if i-number_x >= 0] # генератор разности зн.массива и X больше нуля
minus = [i-number_x for i in array_a if i-number_x < 0] # генератор разности зн.массива и X меньше нуля
maximum = min(plus) if len(plus) > 0 else MAXIMUM+number_x # тренарное условие по поиску ближайшего справа
minimum = max(minus) if len(minus) > 0 else -(MAXIMUM+number_x) # условие по поиску ближайшего слева
# Вывод ближайшего числа X
# Если число X (например 5) имеет два ближайших в обе стороны (4 <- 5 -> 6),
# то будет выведено два числа -> 4 6
if maximum == abs(minimum):
    print(f"-> {minimum+number_x} {maximum+number_x}")
elif maximum < abs(minimum):
    print(f"-> {maximum+number_x}")
elif maximum > abs(minimum):
    print(f"-> {minimum+number_x}")
