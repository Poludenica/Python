#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = int(input('Введите количество чисел: '))
# list_1 = []
# for i in range(n):
#     a = int(input())
#     list_1.append(a)
          
# x = int(input('введите число, повторение которого нужно посчитать: '))
# print((list_1.count(x)))


# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = int(input('Введите количество чисел: '))
# list_1 = []
# for i in range(n):
#     a = int(input())
#     list_1.append(a)
# print(list_1)     
# x = int(input('введите число, к которому нужно найти самое близкое по величине значение: '))

# diff = list_1[-1]
# for i in list_1:
#     if 0 <= (i - x) < diff:
#         diff = (i - x)
#         item = i
# print(f'Ближайшее по величинам число: {item}')


# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#  Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# dic_1 = { 1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'HVWYЫ', 5:'KЖЗХЦЧ', 8: 'JXШЭЮ', 10:'QZФЩЪ'}

# # letter_point = {1: 1, 2: 2, 3: 3,
#                 #  4: 4, 5: 5, 6: 8, 7: 10}

# word = (input("Введите слово на любом языке для подсчета очков: ")).upper()
# points = 0
# for item in word:
#     for key, value in dic_1.items():
#         if item in value:
#             points += key
# print(f"Количество очков за слово {word} равно {points}")