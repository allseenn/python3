# 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из 
# одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются 
# друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам
def syllable(words: str) -> int:
    flag = False
    counter = 0    
    for i in words:
        if i in vowels and flag == False: # Set flag when vowel comes and no previous one
            flag = True
            counter += 1
        elif i in vowels and flag == True: # After one vowel comes another - error code
            return -1
        else: # consonant
            flag = False
    return counter


phrases = [i.lower() for i in input("Enter Viny phrases: ").split()]
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'a', 'e', 'i', 'o', 'u']
vow = -2
for i in phrases:
    if syllable(i) <= 0:  # i syllable -1 "aa"
        print("Пам парам")
        break
    elif vow == -2: #  If first time vow is -2 assighn syllable to it
        vow = syllable(i)
    elif vow != syllable(i): # if prev syllable less 
        print("Пам парам")
        vow = -2
        break 
if vow > 0:  # if -1 "aa" or 0 empty or -2 error 
    print("Парам пам-пам")
elif len(phrases) <= 0: # if no phrases was given
    print("Пам парам")

