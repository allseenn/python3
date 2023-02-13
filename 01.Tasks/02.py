# Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
number = int(input("Enter 3-digit number: "))
print(f"{number} -> {number//100 + number//10%10 + number%10} \
({number//100} + {number//10%10} + {number%10})")