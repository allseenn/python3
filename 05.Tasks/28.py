# - Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#  Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 22 
# 4
def summa(a, b):
    if b == 0:
        return 1
    return a + summa(1, b-1)

number_a = int(input("Enter A: "))
number_b = int(input("Enter B: "))
print(f"{summa(number_a, number_b)}")