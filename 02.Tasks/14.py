# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
number = int(input("Enter a number: "))
power = 1
print(f"{number} -> ", end ="")
while power <= number:
    print(power, end=" ")
    power *= 2
print()
