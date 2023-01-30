# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
n_size = int(input("Enter a number for N: "))
m_size = int(input("Enter a number for M: "))
k_size = int(input("Enter a number for K: "))
if k_size%n_size == 0 and m_size*n_size > k_size:
    print(f"{n_size} {m_size} {k_size} -> yes")
elif k_size%m_size == 0 and n_size*m_size > k_size:
    print(f"{n_size} {m_size} {k_size} -> yes")
else:
    print(f"{n_size} {m_size} {k_size} -> no")