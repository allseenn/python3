# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 
def simple_num(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return "NO"
    return "YES"

n = int(input("Введите число: "))
print(simple_num(n))