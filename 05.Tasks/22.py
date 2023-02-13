# Задача 26: Напишите программу, которая на вход принимает два числа A и B 
# и возводит число А в целую степень B с помощью рекурсии.
# $3^{5}$
# ```
# A = 3; B = 5 -> 243
# A = 2; B = 3 -> 8
def recursion(a, b):
    if b == 0:
        return 1
    return a * recursion(a, b-1)


number_a = int(input("Enter A: "))
number_b = int(input("Enter B: "))
print(f"{recursion(number_a, number_b)}")
