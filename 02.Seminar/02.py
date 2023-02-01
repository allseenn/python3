# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input:     5
# Output:  6
def fib(n):
    res = 1
    count = 1
    while res < n:
        res = res * count
        count += 1
    return count


number = int(input("Enter a number: "))

print(fib(number))