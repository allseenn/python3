# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
import random
n = random.randint(5,9)
orel = 0
reshka = 0
coin = 0
print(f"{n} -> ", end ="")
for i in range(n):
    coin = random.randint(0,1)
    if coin == 1:
         reshka += 1
    else:
        orel +=1
    print(coin, end=" ")
if reshka > orel > 0:
    print(f"\n{orel}")
elif orel > reshka > 0:
    print(f"\n{reshka}")
elif reshka == orel:
     print(f"\n{reshka}")
else:
    print(f"\n{0}")

