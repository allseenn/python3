# Генераторы - не функции!
from sys import getsizeof as gs
# Пример чтения из файла с помощью определения обычных функций
# Чтение файла с помощью функции и разбивка с помощь split
def csv_read_func(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
# Подсчет строк в файле с помощью обычной функции
csv_gen = csv_read_func("laptops.csv")
row_count = 0
for row in (row for row in open("laptops.csv")):
    row_count += 1
print(f"Row count with function is {row_count}")

# Генератор очень похож на функции, но вместо return использует yield, остановка происходит на 
# новой строке row после yield и ждет последующего вызова через новое обращение к генератору
# через csv_gen  
def csv_read_gen(file_name):
    for row in open(file_name, "r"):
        yield row
# Подсчет строк в файле с помощью генератора
csv_gen = csv_read_func("laptops.csv")
# Перематывать генератор вперед можно с помощью функций итерирующих функций, либо с помощью next()
row_count = 0
for row in csv_gen:
    row_count += 1
print(f"Row count with function is {row_count}")
# Функцию верхний генератор можно заменить генератор компрехеншином:
gena = (row for row in open("laptops.csv"))
# А выражение с циклом перебора значений генератора заменим лист компрехеншеном:
print(len([i for i in gena]))
# So 9 lines of code could be replaced by 2

# Генератор генераторов занимают меньше памати,
# чем генераторы списков
# разница только в квадратных и круглых скобках
print(gs([i for i in range(0,1000)]))
print(gs((i for i in range(0,1000))))

import time
start = time.time()

[i for i in range(0,100000000)]
print(time.time() - start)

start = time.time()
(j for j in range(0,100000000))
print(time.time() - start)
