# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# n = int(input('Введите количество чисел для первого множества: '))
# print('введите числа: ')
# list_1 = []
# for i in range(n):
#     a = int(input())
#     list_1.append(a)
# m = int(input('Введите количество чисел для второго множества: '))
# print('введите числа: ')
# list_2 = []
# for i in range(m):
#     a = int(input())
#     list_2.append(a)

# set1 = set(list_1)
# set2 = set(list_2)

# if set1&set2 == set():
#     print("Повторяющихся чисел нет")
# else:
#     print(*('Повторяющиеся числа:', *sorted(list(set1&set2))))

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# number_of_berries_from_bush = [1, 2, 3, 4, 5, 6, 7, 8]
# bush_number = int(input('Введите номер куста: '))
# numbers_of_berries = number_of_berries_from_bush[bush_number-1] + number_of_berries_from_bush[(bush_number - 1)%8-1] + number_of_berries_from_bush[(bush_number + 1)%8-1]

# print(f"Макс. кол-во ягод {numbers_of_berries }, собрано с куста {bush_number}")