# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
from random import randint

n = 6

def recurs(x):
    if x == 0:
        print()
        return
        
    number = randint(0, 100)
    
    print(number,end=" ")
    recurs(x - 1)
    print(number,end=" ")
    

recurs(n)