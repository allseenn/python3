# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит 
# из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9
from random import randint
berry = 10
bush_n = randint(5,10)
# Write to file random string
with open('file.txt', 'w') as data:
    data.write(" ".join(map(str, [randint(1, berry) for _ in range(bush_n)])))
# Read from file string
with open('file.txt', 'r') as data:
    bush_string = data.read()   
print(f"{bush_n} -> {bush_string}")
# Convert from string list to int list
bush_list = list(map(int, bush_string.split()))
berries = 0
for i,_ in enumerate(bush_list):
    if int(bush_list[i-2]+bush_list[i-1]+bush_list[i]) > berries:
        berries = int(bush_list[i-2]+bush_list[i-1]+bush_list[i])
print(berries)